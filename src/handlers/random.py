from telegram import Update
from telegram.ext import ContextTypes
from src.core import PATH_TO_RANDOM_IMAGE, PATH_TO_RANDOM_PROMPT, read_text, OpenAIClient, random_keyboard
import logging

logger = logging.getLogger(__name__)

async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Command /random from user %s", update.effective_chat.id)
    try:
        chat_id = update.effective_chat.id
        await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_RANDOM_IMAGE, "rb"))
        prompt = read_text(PATH_TO_RANDOM_PROMPT)
        client = OpenAIClient()
        fact = await client.ask(user_message=prompt)
        await context.bot.send_message(chat_id=chat_id, text=fact, reply_markup=random_keyboard())
        logger.info("Random fact sent successfully")
    except Exception as e:
        logger.error("Error in /random: %s", e, exc_info=True)
