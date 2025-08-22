from config import TG_BOT_API_KEY
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import start, random_fact, gpt_start, gpt_end, talk_start, talk_set_persona, talk_end, handle_text
from utils import load_messages_for_bot

async def button_handler(update, context):
    data = update.callback_query.data
    if data == "random":
        from handlers import random_fact as _rf
        await _rf(update, context)
    elif data == "end":
        await start(update, context)
    elif data == "gpt_end":
        await gpt_end(update, context, load_messages_for_bot("main"))
    elif data == "talk_einstein":
        await talk_set_persona(update, context, "einstein")
    elif data == "talk_jobs":
        await talk_set_persona(update, context, "jobs")
    elif data == "talk_musk":
        await talk_set_persona(update, context, "musk")
    elif data == "talk_end":
        await talk_end(update, context, load_messages_for_bot("main"))
    await update.callback_query.answer()

app = ApplicationBuilder().token(TG_BOT_API_KEY).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("random", random_fact))
app.add_handler(CommandHandler("gpt", gpt_start))
app.add_handler(CommandHandler("talk", talk_start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
