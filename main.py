from OpenAI_SDK import AI
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

def obtainKeys():
    with open("keys.json", "r") as file:
            keys = json.load(file)
    openAI_key = keys["OPENAI_API_KEY"]
    assistant_id = keys["OPENAI_ASSISTANT"]
    token = keys["TELEGRAM_BOT_TOKEN"]
    return openAI_key, assistant_id, token

def getRespuesta(mensaje):
    openAI_key, assistant_id, token = obtainKeys()
    OpenAi = AI(openAI_key, assistant_id)
    response = OpenAi.interactWithAssistant(mensaje)
    return response

def callTelegramBot():
    openAI_key, assistant_id, token = obtainKeys()
    OpenAi = AI(openAI_key, assistant_id)
    
    async def botAnswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_id = update.message.from_user.id
        message = update.message.text
        response = OpenAi.interactWithAssistant(message, user_id)
        await update.message.reply_text(response)
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT, botAnswer))
    app.run_polling()

callTelegramBot()

# print(getRespuesta("Hola, ¿cómo estás?"))