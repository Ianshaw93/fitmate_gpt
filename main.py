import json
import os
import time
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import functions
from functions import ping_telegram
from record_transcript import add_metrics_to_db, add_transcript_to_db
# from packaging import version
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
client = OpenAI(api_key=OPENAI_API_KEY)

last_chat_time = None

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
    global last_chat_time
    thread_id = chat_request.thread_id
    user_input = chat_request.message
    if not thread_id:
        print("Error: Missing thread_id in /chat")
        raise HTTPException(status_code=400, detail="Missing thread_id")
    print("Received message for thread ID:", thread_id, "Message:", user_input)
    last_chat_time = time.time()
    client.beta.threads.messages.create(thread_id=thread_id, role="user", content=user_input)
    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)
    print("Run started with ID:", run.id)

    return {"run_id": run.id}

@app.post("/check")
async def check_run_status(check_request: CheckRequest):
    print("/check received")
    thread_id = check_request.thread_id
    run_id = check_request.run_id
    if not thread_id or not run_id:
        print("Error: Missing thread_id or run_id in /check")
        raise HTTPException(status_code=400, detail="Missing thread_id or run_id")

    # messages = client.beta.threads.messages.list(thread_id=thread_id)
    # ping_telegram("failed", messages)
    # return {"response": "error"}
    start_time = time.time()
    interval = 0.5
    print("pre loop start:", start_time, "time:", time.time(), "diff:", time.time() - start_time)
    while time.time() - start_time < 8:
    # while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        print("Checking run status:", run_status.status)

        if run_status.status == 'failed' or run_status.status == 'expired':
            # action telegram message
            # TODO: Handle failed runs - if wrong format of request may start death loop
            # likely needs to send to human and ping them
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            ping_telegram(run_status.status, messages)
            return {"response": "error"}


        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            message_content = messages.data[0].content[0].text
            prompt_content = messages.data[1].content[0].text
            # Remove annotations
            print("messages: ", messages)
            print("prompt_content: ", message_content)
            annotations = message_content.annotations
            for annotation in annotations:
                message_content.value = message_content.value.replace(annotation.text, '')
            prompt_annotations = prompt_content.annotations
            for annotation in prompt_annotations:
                prompt_content.value = prompt_content.value.replace(annotation.text, '')
            print("Run completed, returning response")
            # TODO: add response to database
            add_metrics_to_db(thread_id, run_id, starting_date=last_chat_time, time_taken=last_chat_time-time.time(), prompt=prompt_content.value, response=message_content.value, error=False)
            return {"response": message_content.value, "status": "completed"}

        if run_status.status == 'requires_action':
            print("Action in progress...")
            # Handle the function call
            for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                if tool_call.function.name == "create_lead":
                    arguments = json.loads(tool_call.function.arguments)
                    output = functions.create_lead(arguments["name"], arguments["phone"])
                    ping_telegram("client added to follow up spreadsheet", f'Name: {arguments["name"]}, Number: {arguments["phone"]}')
                    client.beta.threads.runs.submit_tool_outputs(thread_id=thread_id, run_id=run_id, tool_outputs=[{"tool_call_id": tool_call.id, "output": json.dumps(output)}])
        time.sleep(interval)

    print("Run timed out")
    return {"response": "timeout"}

