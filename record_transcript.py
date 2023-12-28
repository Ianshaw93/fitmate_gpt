'''
TODO: save to local file with object containing thread_id, run_id, time taken, prompt and response
other file containing: thread_id, date, transcript
'''
from typing import List

# Sample data structure as provided
class Text:
    def __init__(self, value):
        self.value = value

class MessageContentText:
    def __init__(self, text):
        self.text = text

class ThreadMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content

# Simulating the provided data structure
        
# messages = SyncCursorPage[ThreadMessage](data=[ThreadMessage(id='msg_9N4Hs9R0Rtdgp7l0t3tttbzH', assistant_id='asst_bMSKz9noE8Xvq7WDAu5VaMBL', content=[MessageContentText(text=Text(annotations=[TextAnnotationFileCitation(end_index=395, file_citation=TextAnnotationFileCitationFileCitation(file_id='file-g1aLwTukH0NXNFZn8WfV2RT8', quote='Personalized Coaching ● Tailored fitness plans to suit individual needs and schedules of busy entrepreneurs and home 
# moms. ● Regular progress tracking and adjustments to ensure optimal results. ● Emphasis on sustainable and balanced lifestyle changes'), start_index=384, text='s a busy en', type='file_citation')], value="The fitness programs offer personalized coaching, which includes creating tailored fitness plans 
# to fit your individual needs and schedule. Regular progress tracking and adjustments are part of the service to ensure you're always heading toward optimal results. One-to-one coaching is central to the approach of these programs, to ensure a sustainable and balanced lifestyle for you as a busy entrepreneur or stay-at-home mom【11†source】. If you're ready to get started or have any further questions, feel free to reach out!"), type='text')], created_at=1703334559, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_h6XJpc9x2SpYq09FGDMXOdEe', thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_erlNpi7Us3H0GddGQY1uZfvF', assistant_id=None, content=[MessageContentText(text=Text(annotations=[], value='do I get any one to one coaching in the programmes?'), type='text')], created_at=1703334556, file_ids=[], metadata={}, object='thread.message', role='user', run_id=None, thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_qIf56hVDaeZPicP1s5yKjTjn', assistant_id='asst_bMSKz9noE8Xvq7WDAu5VaMBL', content=[MessageContentText(text=Text(annotations=[TextAnnotationFileCitation(end_index=395, file_citation=TextAnnotationFileCitationFileCitation(file_id='file-g1aLwTukH0NXNFZn8WfV2RT8', quote='Personalized Coaching ● Tailored fitness plans to suit individual needs and schedules of busy entrepreneurs and home moms. ● Regular progress tracking and adjustments to ensure optimal results. ● Emphasis on sustainable and balanced lifestyle changes'), start_index=384, text='ey is effec', type='file_citation')], value="Yes, you do! The fitness programs provide personalized coaching with tailored fitness plans, ensuring they match your individual needs. The one-to-one coaching aspect includes regular progress tracking and adjustments to guarantee optimal results, all while focusing on sustainable and balanced lifestyle changes【11†source】. This approach is ideal for ensuring that your fitness journey is effective and aligns with your busy schedule. If you're interested, we can get you started!"), type='text')], created_at=1703334456, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_MfxAKcscVmsUxyIQ1LgmHFXE', thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_2RwmAt0qNAQj3ZStbilIYPYe', assistant_id=None, content=[MessageContentText(text=Text(annotations=[], value='do I get any one to one coaching in the programmes?'), type='text')], created_at=1703334453, file_ids=[], metadata={}, object='thread.message', role='user', run_id=None, thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_CokA8o8mt73Cb9DvT9hEsTKN', assistant_id='asst_bMSKz9noE8Xvq7WDAu5VaMBL', content=[MessageContentText(text=Text(annotations=[TextAnnotationFileCitation(end_index=395, file_citation=TextAnnotationFileCitationFileCitation(file_id='file-g1aLwTukH0NXNFZn8WfV2RT8', quote='Personalized Coaching ● Tailored fitness plans to suit individual needs and schedules of busy entrepreneurs and home moms. ● Regular progress tracking and adjustments to ensure optimal results. ● Emphasis on sustainable and balanced lifestyle changes'), start_index=384, text='pproach, I ', type='file_citation')], value="Yes, the programs offer one-to-one personalized coaching. This includes fitness plans that are tailored to 
# your specific needs and schedule, regular progress tracking, and necessary adjustments to ensure you get the best results. The coaching emphasizes sustainable lifestyle changes for busy entrepreneurs and stay-at-home moms【11†source】. If you're interested in this personalized approach, I can assist you with the next steps!"), type='text')], created_at=1703334196, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_mB1IV808qutmvt9y3ooSsr8h', thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_buBXKsRVE7ou3cOWhv2hYZ3T', assistant_id=None, content=[MessageContentText(text=Text(annotations=[], value='do I get any one to one coaching in the programmes?'), type='text')], created_at=1703334194, file_ids=[], metadata={}, object='thread.message', role='user', run_id=None, thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_0FVTkCsQchIhq8G7kmmFpLQl', assistant_id='asst_bMSKz9noE8Xvq7WDAu5VaMBL', content=[MessageContentText(text=Text(annotations=[TextAnnotationFileCitation(end_index=395, file_citation=TextAnnotationFileCitationFileCitation(file_id='file-g1aLwTukH0NXNFZn8WfV2RT8', quote='Personalized Coaching ● Tailored fitness plans to suit individual needs and schedules of busy entrepreneurs and home moms. ● Regular progress tracking and adjustments to ensure optimal results. ● Emphasis on sustainable and balanced lifestyle changes'), start_index=384, text='【12†source】', type='file_citation')], value="Definitely! The programs include personalized coaching with fitness plans tailored to individual needs and schedules, regular progress tracking, and adjustments to ensure you achieve optimal results. There's an emphasis on creating sustainable and balanced lifestyle changes. Daniël provides regular feedback and interaction to maintain your progress and satisfaction with the program【12†source】. If you're looking for that personalized touch in your fitness journey, you're in the 
# right place!"), type='text')], created_at=1703334177, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_mVsqsevk4Du4ukV2NQXdAdIQ', thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_vFabrKjMg24Mijjj3wE7VCjd', assistant_id=None, content=[MessageContentText(text=Text(annotations=[], value='do I get any one to one coaching in the programmes?'), type='text')], created_at=1703334172, file_ids=[], metadata={}, object='thread.message', role='user', run_id=None, thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_PEzIbu9Ae3pmgX1wOhu47XgC', assistant_id='asst_bMSKz9noE8Xvq7WDAu5VaMBL', content=[MessageContentText(text=Text(annotations=[], value="Yes, Daniël Stegehuis's online fitness programs serve clients globally, including the US. These programs are specifically designed to fit into the busy schedules of entrepreneurs and stay-at-home moms. You can access the workouts online from anywhere, which makes it convenient for clients in the US or any other location. If you're ready to start 
# or have any other questions, let me know!"), type='text')], created_at=1703333978, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_rcACnZm8L1HyzR9aPqGBxtcg', thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP'), ThreadMessage(id='msg_UGO3uviCq6PM2X3evCw4nu1a', assistant_id=None, content=[MessageContentText(text=Text(annotations=[], value='do you serve the US?'), type='text')], created_at=1703333973, file_ids=[], metadata={}, object='thread.message', role='user', run_id=None, thread_id='thread_pYwe5OJRu9SVGefQvZ3jnZVP')], object='list', first_id='msg_9N4Hs9R0Rtdgp7l0t3tttbzH', last_id='msg_UGO3uviCq6PM2X3evCw4nu1a', has_more=False)
messages = [
    ThreadMessage('assistant', [MessageContentText(Text("Assistant's message"))]),
    ThreadMessage('user', [MessageContentText(Text("do you serve the US?"))]),
    ThreadMessage('assistant', [MessageContentText(Text("Another assistant's message"))]),
    ThreadMessage('user', [MessageContentText(Text("Another user's message"))])
]

# Function to find the lowest index with role 'user'
def find_lowest_user_index(messages: List[ThreadMessage]) -> int:
    for index, message in enumerate(messages):
        if message.role == 'user':
            return index
    return -1  # Return -1 if no user message is found

# Find the lowest index with role 'user'
lowest_user_index = find_lowest_user_index(messages)
print(lowest_user_index)
messages[0].content[0].text.value



import json

def add_metrics_to_db(thread_id, run_id, starting_date, time_taken, prompt, response, error):
    
    file_path = 'metrics.json'
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}


    # Updating the existing JSON object with new data
    # For demonstration, adding a new message object
    new_message = {
        "thread_id": thread_id,
        "run_id": run_id,
        "starting_date": starting_date,
        "time_taken": time_taken,
        "prompt": prompt,
        "response": response,
        "error": error

    }

    # Check if existing_data is a list and add the new message
    if isinstance(existing_data, list):
        existing_data.append(new_message)
    else:
        existing_data = [new_message]  # Create a new list with the new message if existing data is not a list

    # Saving the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
        # with open('metrics.txt', 'a') as f:
        #     f.write(f'{thread_id},{run_id},{starting_date},{time_taken},{prompt},{response}, {error}\n')


def add_transcript_to_db(thread_id, date, transcript):
    with open('transcript.txt', 'a') as f:
        f.write(f'{thread_id},{date},{transcript}\n')

if __name__ == '__main__':

    add_metrics_to_db(thread_id='msg_9N4Hs9R0Rtdgp7l0t3tttbzH', run_id='run_mB1IV808qutmvt9y3ooSsr8h', starting_date=1703334559, time_taken=1703334650, prompt='do you serve the US?', response="Assistant's message", error=False)
