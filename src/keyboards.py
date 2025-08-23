from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def random_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Хочу ще факт", callback_data="random")],
        [InlineKeyboardButton("Закінчити", callback_data="end")],
    ])

def gpt_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Закінчити", callback_data="gpt_end")]
    ])

def talk_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Альберт Ейнштейн", callback_data="talk_einstein")],
        [InlineKeyboardButton("Стів Джобс", callback_data="talk_jobs")],
        [InlineKeyboardButton("Ілон Маск", callback_data="talk_musk")],
    ])

def talk_end_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Закінчити", callback_data="talk_end")]
    ])

def quiz_topics_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Наука", callback_data="quiz_topic_science")],
        [InlineKeyboardButton("Історія", callback_data="quiz_topic_history")],
        [InlineKeyboardButton("Кіно", callback_data="quiz_topic_movies")],
        [InlineKeyboardButton("Медицина", callback_data="quiz_topic_medicine")]
    ])

def quiz_actions_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Ще питання", callback_data="quiz_next")],
        [InlineKeyboardButton("Змінити тему", callback_data="quiz_change")],
        [InlineKeyboardButton("Закінчити", callback_data="quiz_end")],
    ])

def translate_langs_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("EN", callback_data="translate_language_en"),
         InlineKeyboardButton("DE", callback_data="translate_language_de"),
         InlineKeyboardButton("PL", callback_data="translate_language_pl"),
         InlineKeyboardButton("ES", callback_data="translate_language_es")],
        [InlineKeyboardButton("UA", callback_data="translate_language_uk")],
        [InlineKeyboardButton("Закінчити", callback_data="translate_end")]
    ])

def translate_actions_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Змінити мову", callback_data="translate_change")],
        [InlineKeyboardButton("Закінчити", callback_data="translate_end")]
    ])

