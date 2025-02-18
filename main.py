from OpenAI_SDK import AI
import json

with open("keys.json", "r") as file:
    keys = json.load(file)

openAI_key = keys["OPENAI_API_KEY"]
assistant_id = keys["OPENAI_ASSISTANT"]

OpenAi = AI(openAI_key, assistant_id)
response = OpenAi.interactWithAssistant("Hola!!")

print(response)