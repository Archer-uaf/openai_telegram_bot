from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from pathlib import Path
from src.config import PATH_TO_TALK_IMAGE, PATH_TO_TALK_PROMPTS
from src.openapi_client import OpenAIClient

def talk_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Альберт Ейнштейн", callback_data="talk_einstein")],
        [InlineKeyboardButton("Стів Джобс", callback_data="talk_jobs")],
        [InlineKeyboardButton("Ілон Маск", callback_data="talk_musk")],
    ])

def end_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("Закінчити", callback_data="talk_end")]])

def read_text(path: Path) -> str:
    return Path(path).read_text(encoding="utf-8").strip()

async def talk_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.user_data["mode"] = None
    context.user_data["talk_prompt"] = None
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_TALK_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Оберіть особистість:", reply_markup=talk_keyboard())

async def talk_set_persona(update: Update, context: ContextTypes.DEFAULT_TYPE, persona: str):
    path = PATH_TO_TALK_PROMPTS / f"{persona}.txt"
    if not path.exists():
        await update.callback_query.message.reply_text("Файл промпта не знайдено.")
        await update.callback_query.answer()
        return
    context.user_data["talk_prompt"] = read_text(path)
    context.user_data["mode"] = "talk"
    await update.callback_query.message.reply_text("Починаємо діалог. Напишіть повідомлення 👇", reply_markup=end_keyboard())
    await update.callback_query.answer()

async def talk_end(update: Update, context: ContextTypes.DEFAULT_TYPE, main_text: str):
    context.user_data["mode"] = None
    context.user_data["talk_prompt"] = None
    await update.callback_query.message.reply_text(main_text)
    await update.callback_query.answer()
