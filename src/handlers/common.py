from telegram import Update
from telegram.ext import ContextTypes
from src.core.openai_client import OpenAIClient
from src.core.keyboards import gpt_keyboard, quiz_actions_keyboard, translate_actions_keyboard, recommendations_actions_keyboard
from src.core.config import PATH_TO_QUIZ_PROMPT, PATH_TO_TRANSLATE_PROMPT, PATH_TO_RECOMMENDATIONS_PROMPT
from src.core.utils import read_text

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get("mode")
    if mode == "gpt":
        client = OpenAIClient()
        answer = await client.ask(user_message=update.message.text)
        await update.message.reply_text(answer, reply_markup=gpt_keyboard())
        return

    if mode == "talk" and context.user_data.get("talk_prompt"):
        client = OpenAIClient()
        answer = await client.ask(user_message=update.message.text, system_prompt=context.user_data["talk_prompt"])
        from src.core.keyboards import talk_end_keyboard
        await update.message.reply_text(answer, reply_markup=talk_end_keyboard())
        return

    if mode == "quiz" and context.user_data.get("quiz_question"):
        client = OpenAIClient()
        question = context.user_data["quiz_question"]
        user_ans = update.message.text.strip()

        eval_prompt = read_text(PATH_TO_QUIZ_PROMPT)
        user_msg = f"Питання: {question}\nВідповідь користувача: {user_ans}\nОціни."
        verdict = await client.ask(user_message=user_msg, system_prompt=eval_prompt)

        await update.message.reply_text(verdict, reply_markup=quiz_actions_keyboard())
        context.user_data["quiz_question"] = None

    if mode == "translate" and context.user_data.get("translate_language"):
        client = OpenAIClient()
        lang = context.user_data["translate_language"]
        sys = read_text(PATH_TO_TRANSLATE_PROMPT)
        user_msg = f"Target language: {lang}\nText: {update.message.text.strip()}"
        translated = await client.ask(user_message=user_msg, system_prompt=sys)
        await update.message.reply_text(translated, reply_markup=translate_actions_keyboard())
        return
    if mode == "recommendations" and context.user_data.get("recommendations_genre"):
        client = OpenAIClient()
        sys = read_text(PATH_TO_RECOMMENDATIONS_PROMPT)
        genre = context.user_data["recommendations_genre"]
        prefs = update.message.text.strip()
        context.user_data["recommendations_last_query"] = prefs
        text = await client.ask(user_message=f"genre: {genre}\npreferences: {prefs}", system_prompt=sys)
        await update.message.reply_text(text, reply_markup=recommendations_actions_keyboard())
        return

