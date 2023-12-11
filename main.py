import json
import os
import time
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import functions

# from packaging import version
from dotenv import load_dotenv

load_dotenv()
# required_version = version.parse("1.1.1")
# current_version = version.parse(openai.__version__)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# if current_version < required_version:
#     raise ValueError(
#         f"Error: OpenAI version {openai.__version__} is less than the required version 1.1.1"
#     )
# else:
#     print("OpenAI version is compatible.")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
client = OpenAI(api_key=OPENAI_API_KEY)

# Load assistant ID from file or create new one
assistant_id = functions.create_assistant(client)
print("Assistant created with ID:", assistant_id)

class ChatRequest(BaseModel):
    thread_id: str
    message: str = ''

class CheckRequest(BaseModel):
    thread_id: str
    run_id: str

@app.get("/")
async def quick_test():

    return {"thread_id": "test"}


@app.get("/start")
async def start_conversation():
    thread = client.beta.threads.create()
    print("New conversation started with thread ID:", thread.id)
    return {"thread_id": thread.id}

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    thread_id = chat_request.thread_id
    user_input = chat_request.message
    if not thread_id:
        print("Error: Missing thread_id in /chat")
        raise HTTPException(status_code=400, detail="Missing thread_id")
    print("Received message for thread ID:", thread_id, "Message:", user_input)

    client.beta.threads.messages.create(thread_id=thread_id, role="user", content=user_input)
    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)
    print("Run started with ID:", run.id)
    return {"run_id": run.id}

@app.post("/check")
async def check_run_status(check_request: CheckRequest):
    thread_id = check_request.thread_id
    run_id = check_request.run_id
    if not thread_id or not run_id:
        print("Error: Missing thread_id or run_id in /check")
        raise HTTPException(status_code=400, detail="Missing thread_id or run_id")

    start_time = time.time()
    while time.time() - start_time < 9:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        print("Checking run status:", run_status.status)

        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            message_content = messages.data[0].content[0].text
            # Remove annotations
            annotations = message_content.annotations
            for annotation in annotations:
                message_content.value = message_content.value.replace(annotation.text, '')
            print("Run completed, returning response")
            return {"response": message_content.value, "status": "completed"}

        if run_status.status == 'requires_action':
            print("Action in progress...")
            # Handle the function call
            for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                if tool_call.function.name == "create_lead":
                    arguments = json.loads(tool_call.function.arguments)
                    output = functions.create_lead(arguments["name"], arguments["phone"])
                    client.beta.threads.runs.submit_tool_outputs(thread_id=thread_id, run_id=run_id, tool_outputs=[{"tool_call_id": tool_call.id, "output": json.dumps(output)}])
        time.sleep(1)

    print("Run timed out")
    return {"response": "timeout"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)
