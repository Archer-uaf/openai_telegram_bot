from config import PATH_TO_RESOURCES
from config import PATH_TO_PROMPTS
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def load_messages_for_bot(name: str) -> str:
    with open(PATH_TO_RESOURCES / f"{name}.txt", encoding="utf-8") as file:
        return file.read()

def random_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Хочу ще факт", callback_data="random")],
        [InlineKeyboardButton("Закінчити", callback_data="end")],
    ])

def read_text(path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()