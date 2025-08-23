from pathlib import Path
import os
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

PATH_TO_ENV = SRC_DIR / ".env"
load_dotenv(PATH_TO_ENV)

PATH_TO_RESOURCES = SRC_DIR / "resources"
PATH_TO_IMAGES = PATH_TO_RESOURCES / "images"
PATH_TO_PROMPTS = PATH_TO_RESOURCES / "prompts"

PATH_TO_RANDOM_IMAGE = PATH_TO_IMAGES / "random.jpg"
PATH_TO_RANDOM_PROMPT = PATH_TO_PROMPTS / "random.txt"

PATH_TO_GPT_IMAGE = PATH_TO_IMAGES / "gpt.jpg"

PATH_TO_TALK_IMAGE = PATH_TO_IMAGES / "talk.jpg"
PATH_TO_TALK_PROMPTS = PATH_TO_PROMPTS / "talk"

PATH_TO_QUIZ_IMAGE = PATH_TO_IMAGES / "quiz.jpg"
PATH_TO_QUIZ_PROMPT = PATH_TO_PROMPTS / "quiz.txt"

PATH_TO_TRANSLATE_IMAGE = PATH_TO_IMAGES / "translate.jpeg"
PATH_TO_TRANSLATE_PROMPT = PATH_TO_PROMPTS / "translate.txt"

PATH_TO_RECOMMENDATIONS_IMAGE = PATH_TO_IMAGES / "recommendations.png"
PATH_TO_RECOMMENDATIONS_PROMPT = PATH_TO_PROMPTS / "recommendations.txt"


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TG_BOT_API_KEY = os.getenv("TG_BOT_API_KEY")
