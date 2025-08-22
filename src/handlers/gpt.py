from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from src.config import PATH_TO_GPT_IMAGE
from src.openapi_client import OpenAIClient

def gpt_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("Закінчити", callback_data="gpt_end")]])

async def gpt_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.user_data["mode"] = "gpt"
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_GPT_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Ви почали діалог з ChatGPT. Напишіть повідомлення 👇", reply_markup=gpt_keyboard())

async def gpt_end(update: Update, context: ContextTypes.DEFAULT_TYPE, main_text: str):
    context.user_data["mode"] = None
    await update.callback_query.message.reply_text(main_text)
    await update.callback_query.answer()
