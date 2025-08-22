from telegram import Update
from telegram.ext import ContextTypes
from utils import load_messages_for_bot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_messages_for_bot("main")
    if update.callback_query:
        await update.callback_query.edit_message_text(text)
    else:
        await update.message.reply_text(text)