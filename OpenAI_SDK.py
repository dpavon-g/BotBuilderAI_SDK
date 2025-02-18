from openai import OpenAI

class AI:
    def __init__(self, api_key, assistant_id):
        self.api_key = api_key
        self.assistant_id = assistant_id
    
    def interactWithAssistant(self, message, threadID = None):
        client = OpenAI(api_key=self.api_key)
        if threadID is None:
            thread = client.beta.threads.create()
            threadID = thread.id
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