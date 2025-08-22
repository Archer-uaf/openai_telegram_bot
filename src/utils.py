from config import PATH_TO_RESOURCES
from config import PATH_TO_PROMPTS

def load_messages_for_bot(name: str) -> str:
    with open(PATH_TO_RESOURCES / f"{name}.txt", encoding="utf-8") as file:
        return file.read()

def read_text(path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()