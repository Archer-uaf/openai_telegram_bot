from telegram import Update
from telegram.ext import ContextTypes
from src.core.config import PATH_TO_TRANSLATE_IMAGE, PATH_TO_TRANSLATE_PROMPT
from src.core.keyboards import translate_langs_keyboard
from src.core.utils import read_text

async def translate_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.user_data["mode"] = None
    context.user_data["translate_language"] = None
    context.user_data["translate_prompt"] = read_text(PATH_TO_TRANSLATE_PROMPT)
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_TRANSLATE_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Оберіть мову перекладу:", reply_markup=translate_langs_keyboard())

async def translate_set_language(update: Update, context: ContextTypes.DEFAULT_TYPE, lang: str):
    context.user_data["mode"] = "translate"
    context.user_data["translate_language"] = lang
    await update.callback_query.message.reply_text(f"Введіть текст для перекладу на {lang.upper()}:")
    await update.callback_query.answer()

async def translate_end(update: Update, context: ContextTypes.DEFAULT_TYPE, main_text: str):
    context.user_data["mode"] = None
    context.user_data["translate_language"] = None
    await update.callback_query.message.reply_text(main_text)
    await update.callback_query.answer()
