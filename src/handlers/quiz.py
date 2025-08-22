from telegram import Update
from telegram.ext import ContextTypes
from src.config import PATH_TO_QUIZ_IMAGE
from src.keyboards import quiz_topics_keyboard, quiz_actions_keyboard
from src.openapi_client import OpenAIClient
import logging

logger = logging.getLogger(__name__)

TOPIC_MAP = {
    "science": "science",
    "history": "history",
    "movies": "movies",
    "medicine": "medicine"
}

async def quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.user_data["mode"] = None
    context.user_data["quiz_topic"] = None
    context.user_data["quiz_question"] = None
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_QUIZ_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Оберіть тему квізу:", reply_markup=quiz_topics_keyboard())

async def quiz_set_topic(update: Update, context: ContextTypes.DEFAULT_TYPE, topic_key: str):
    context.user_data["mode"] = "quiz"
    context.user_data["quiz_topic"] = TOPIC_MAP[topic_key]
    context.user_data["quiz_question"] = None
    await quiz_next_question(update, context)


async def quiz_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.user_data.get("quiz_topic")
    logger.info("User %s requested next quiz question (topic=%s)", update.effective_chat.id, topic)
    if not topic:
        return
    client = OpenAIClient()
    prompt = (
        f"Дай цікаве питання по темі '{topic}' українською. Питання повинні бути цікаві і різноманітні"
        "Надай тільки коротке питання у форматі вікторини."
    )
    question = await client.ask(user_message=prompt, system_prompt="You are a concise quiz generator.")
    context.user_data["quiz_question"] = question.strip()
    chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text=f"Питання:\n{context.user_data['quiz_question']}")

async def quiz_end(update: Update, context: ContextTypes.DEFAULT_TYPE, end_text: str):
    context.user_data["mode"] = None
    context.user_data["quiz_topic"] = None
    context.user_data["quiz_question"] = None
    await update.callback_query.message.reply_text(end_text)
    await update.callback_query.answer()

