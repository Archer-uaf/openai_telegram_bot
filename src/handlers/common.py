from telegram import Update
from telegram.ext import ContextTypes
from src.openapi_client import OpenAIClient
from src.keyboards import gpt_keyboard, quiz_actions_keyboard
import re
from src.config import PATH_TO_QUIZ_PROMPT
from src.utils import read_text

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
        from src.keyboards import talk_end_keyboard
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

