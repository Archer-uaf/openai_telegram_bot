import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from src.app.logs import setup_logging
from src.core import (
    TG_BOT_API_KEY, load_messages_for_bot,
    quiz_topics_keyboard, translate_langs_keyboard, recommendations_genre_keyboard,
)
from src.handlers import (
    start, random_fact,
    gpt_start, gpt_end,
    talk_start, talk_set_persona, talk_end,
    quiz_start, quiz_set_topic, quiz_next_question, quiz_end,
    translate_start, translate_set_language, translate_end,
    recommendations_start, recommendations_set_genre, recommendations_more, recommendations_end,
    handle_text,
)


setup_logging()
logger = logging.getLogger(__name__)
logger.info("Bot starting...")

async def button_handler(update, context):
    data = update.callback_query.data
    if data == "random":
        await random_fact(update, context)

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

    elif data == "quiz_topic_science":
        await quiz_set_topic(update, context, "science")
        await update.callback_query.answer()
    elif data == "quiz_topic_history":
        await quiz_set_topic(update, context, "history")
        await update.callback_query.answer()
    elif data == "quiz_topic_movies":
        await quiz_set_topic(update, context, "movies")
        await update.callback_query.answer()
    elif data == "quiz_topic_medicine":
        await quiz_set_topic(update, context, "medicine")
        await update.callback_query.answer()
    elif data == "quiz_next":
        await quiz_next_question(update, context)
        await update.callback_query.answer()
    elif data == "quiz_change":
        from src.core.keyboards import quiz_topics_keyboard
        await update.callback_query.message.reply_text("Оберіть тему:", reply_markup=quiz_topics_keyboard())
        await update.callback_query.answer()
    elif data == "quiz_end":
        await quiz_end(update, context, load_messages_for_bot("main"))
        return

    elif data == "translate_language_en":
        await translate_set_language(update, context, "en")
    elif data == "translate_language_de":
        await translate_set_language(update, context, "de")
    elif data == "translate_language_pl":
        await translate_set_language(update, context, "pl")
    elif data == "translate_language_es":
        await translate_set_language(update, context, "es")
    elif data == "translate_language_uk":
        await translate_set_language(update, context, "uk")
    elif data == "translate_change":
        await update.callback_query.message.reply_text("Оберіть мову перекладу:", reply_markup=translate_langs_keyboard())
        await update.callback_query.answer()
    elif data == "translate_end":
        await translate_end(update, context, load_messages_for_bot("main")); return

    elif data == "recommendations_genre_action":
        await recommendations_set_genre(update, context, "action")
    elif data == "recommendations_genre_comedy":
        await recommendations_set_genre(update, context, "comedy")
    elif data == "recommendations_genre_drama":
        await recommendations_set_genre(update, context, "drama")
    elif data == "recommendations_genre_horror":
        await recommendations_set_genre(update, context, "horror")
    elif data == "recommendations_genre_scifi":
        await recommendations_set_genre(update, context, "sci-fi")
    elif data == "recommendations_genre_end":
        await update.callback_query.message.reply_text(load_messages_for_bot("main"))
        await update.callback_query.answer()
    elif data == "recommendations_another_genre":
        from src.core.keyboards import recommendations_genre_keyboard
        await update.callback_query.message.reply_text("Оберіть жанр:", reply_markup=recommendations_genre_keyboard())
        await update.callback_query.answer()
    elif data == "recommendations_another_film":
        await recommendations_more(update, context)
    elif data == "recommendations_end":
        await recommendations_end(update, context, load_messages_for_bot("main"))
        return

    await update.callback_query.answer()

app = ApplicationBuilder().token(TG_BOT_API_KEY).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("random", random_fact))
app.add_handler(CommandHandler("gpt", gpt_start))
app.add_handler(CommandHandler("talk", talk_start))
app.add_handler(CommandHandler("quiz", quiz_start))
app.add_handler(CommandHandler("translate", translate_start))
app.add_handler(CommandHandler("recommendations", recommendations_start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
