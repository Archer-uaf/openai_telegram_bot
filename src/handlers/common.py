from telegram import Update
from telegram.ext import ContextTypes
from src.openapi_client import OpenAIClient
from src.utils import load_messages_for_bot
from src.handlers.gpt import gpt_keyboard
from src.handlers.talk import end_keyboard

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get("mode")
    if mode == "gpt":
        client = OpenAIClient()
        answer = await client.ask(user_message=update.message.text)
        await update.message.reply_text(answer, reply_markup=gpt_keyboard())
    elif mode == "talk" and context.user_data.get("talk_prompt"):
        client = OpenAIClient()
        answer = await client.ask(user_message=update.message.text, system_prompt=context.user_data["talk_prompt"])
        await update.message.reply_text(answer, reply_markup=end_keyboard())
