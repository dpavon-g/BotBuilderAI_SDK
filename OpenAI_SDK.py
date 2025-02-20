from openai import OpenAI
import json

class AI:
    
    def getThreadID(self, user_id, client):
        try: 
            with open("threads.json", "r") as file:
                threads = json.load(file)
        except FileNotFoundError:
            threads = {}
            threads[str(user_id)] = client.beta.threads.create().id
            with open("threads.json", "w") as file:
                json.dump(threads, file)
            return threads[str(user_id)]
        
        if str(user_id) in threads:
            return threads[str(user_id)]
        else:
            threads[str(user_id)] = client.beta.threads.create().id
            with open("threads.json", "w") as file:
                json.dump(threads, file)
            return threads[str(user_id)]
    
    def __init__(self, api_key, assistant_id):
        self.api_key = api_key
        self.assistant_id = assistant_id
    
    def interactWithAssistant(self, message, user_id = None):
        client = OpenAI(api_key=self.api_key)
        
        threadID = self.getThreadID(user_id, client)

        message = client.beta.threads.messages.create(
            thread_id=threadID,
            role="user",
            content=message
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=threadID,
            assistant_id=self.assistant_id,
        )
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=threadID
            )
            for message in messages:
                for content_block in message.content:
                    if content_block.type == 'text':
                        return(content_block.text.value)
        else:
            return "Error. No se ha podido obtener el mensaje"