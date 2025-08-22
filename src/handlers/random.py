from telegram import Update
from telegram.ext import ContextTypes
from config import PATH_TO_RANDOM_IMAGE, PATH_TO_RANDOM_PROMPT
from utils import read_text, random_keyboard
from openapi_client import OpenAIClient

async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_RANDOM_IMAGE, "rb"))
    prompt = read_text(PATH_TO_RANDOM_PROMPT)
    client = OpenAIClient()
    fact = await client.ask(user_message=prompt)
    await context.bot.send_message(chat_id=chat_id, text=fact, reply_markup=random_keyboard())