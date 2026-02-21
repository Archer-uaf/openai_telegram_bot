from telegram import Update
from telegram.ext import ContextTypes
from src.core.config import PATH_TO_RECOMMENDATIONS_IMAGE, PATH_TO_RECOMMENDATIONS_PROMPT
from src.core.keyboards import recommendations_genre_keyboard, recommendations_actions_keyboard
from src.core.utils import read_text
from src.core.openai_client import OpenAIClient

async def recommendations_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.user_data["mode"] = None
    context.user_data["recommendations_genre"] = None
    context.user_data["recommendations_prompt"] = read_text(PATH_TO_RECOMMENDATIONS_PROMPT)
    context.user_data["recommendations_notinteresting"] = []
    context.user_data["recommendations_last_query"] = ""
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_RECOMMENDATIONS_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Оберіть жанр:", reply_markup=recommendations_genre_keyboard())

async def recommendations_set_genre(update: Update, context: ContextTypes.DEFAULT_TYPE, genre: str):
    context.user_data["mode"] = "recommendations"
    context.user_data["recommendations_genre"] = genre
    await update.callback_query.message.reply_text("Опиши свої побажання до фільму")
    await update.callback_query.answer()

async def recommendations_more(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("recommendations_last_query"):
        await update.callback_query.answer()
        return
    sys = context.user_data.get("recommendations_prompt", "")
    genre = context.user_data.get("recommendations_genre", "")
    prefs = context.user_data["recommendations_last_query"]
    client = OpenAIClient()
    text = await client.ask(user_message=f"genre: {genre}\npreferences: {prefs}", system_prompt=sys)
    await update.callback_query.message.reply_text(text, reply_markup=recommendations_actions_keyboard())
    await update.callback_query.answer()

async def recommendations_end(update: Update, context: ContextTypes.DEFAULT_TYPE, main_text: str):
    context.user_data["mode"] = None
    context.user_data["recommendations_genre"] = None
    context.user_data["recommendations_last_query"] = ""
    await update.callback_query.message.reply_text(main_text)
    await update.callback_query.answer()


