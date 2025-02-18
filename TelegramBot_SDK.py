from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import json

class TelegramBot:
    def __init__(self, openAI_key, assistant_id, token):
        self.OpenAi = AI(openAI_key, assistant_id)
        self.token = token

    async def botAnswer(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = self.OpenAi.interactWithAssistant(update.message.text)
        await update.message.reply_text(response)

    def main(self):
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(MessageHandler(filters.TEXT, self.botAnswer))
        app.run_polling()