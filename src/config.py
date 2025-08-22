from pathlib import Path
import os
from dotenv import load_dotenv

# env
BASE_DIR = Path(__file__).parent.parent
PATH_TO_ENV = BASE_DIR / ".env"
load_dotenv(PATH_TO_ENV)
PATH_TO_RESOURCES = BASE_DIR / "src" / "resources"
PATH_TO_PROMPTS = PATH_TO_RESOURCES / "prompts"
PATH_TO_IMAGES = PATH_TO_RESOURCES / "images"

# keys
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TG_BOT_API_KEY = os.environ["TG_BOT_API_KEY"]

# feature-specific
PATH_TO_RANDOM_IMAGE = PATH_TO_IMAGES / "random.jpg"
PATH_TO_GPT_IMAGE = PATH_TO_IMAGES / "gpt.jpg"
PATH_TO_RANDOM_PROMPT = PATH_TO_PROMPTS / "random.txt"
PATH_TO_TALK_IMAGE = PATH_TO_IMAGES / "talk.jpg"
PATH_TO_TALK_PROMPTS = PATH_TO_PROMPTS / "talk"
