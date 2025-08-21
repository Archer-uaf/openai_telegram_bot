from config import TG_BOT_API_KEY
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from utils import load_messages_for_bot, read_text, random_keyboard
from openapi_client import OpenAIClient
from config import PATH_TO_RANDOM_PROMPT
from config import PATH_TO_RANDOM_IMAGE
from config import PATH_TO_GPT_IMAGE



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_messages_for_bot("main")
    if update.callback_query:
        await update.callback_query.edit_message_text(text)
    else:
        await update.message.reply_text(text)


async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_RANDOM_IMAGE, "rb"))
    prompt = read_text(PATH_TO_RANDOM_PROMPT)
    client = OpenAIClient()
    fact = await client.ask(user_message=prompt)
    await context.bot.send_message(chat_id=chat_id, text=fact, reply_markup=random_keyboard())

async def gpt_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo=open(PATH_TO_GPT_IMAGE, "rb"))
    await context.bot.send_message(chat_id=chat_id, text="Напишіть повідомлення для ChatGPT")
    context.user_data["mode"] = "gpt"


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("mode") == "gpt":
        client = OpenAIClient()
        answer = await client.ask(user_message=update.message.text)
        await update.message.reply_text(answer)
        context.user_data["mode"] = None
        await update.message.reply_text(load_messages_for_bot("main"))


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data == "random":
        await random_fact(update, context)
    elif data == "end":
        await start(update, context)
    await update.callback_query.answer()


app = ApplicationBuilder().token(TG_BOT_API_KEY).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("random", random_fact))
app.add_handler(CommandHandler("gpt", gpt_start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()