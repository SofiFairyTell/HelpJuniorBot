import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALICE_API_KEY = os.getenv("ALICE_API_KEY")
ALICE_FOLDER_ID = os.getenv("ALICE_FOLDER_ID")
ALICE_MODEL_URI = os.getenv("ALICE_MODEL_URI", "aliceai-llm/latest")

MAX_HISTORY_MESSAGES = 10
HISTORY_FILE = "chat_history.json"

if not ALICE_API_KEY or not ALICE_FOLDER_ID or not BOT_TOKEN:
    raise RuntimeError(
        "Не заданы переменные окружения. Проверьте файл .env в корне проекта: "
        f"BOT_TOKEN={bool(BOT_TOKEN)}, ALICE_API_KEY={bool(ALICE_API_KEY)}, "
        f"ALICE_FOLDER_ID={bool(ALICE_FOLDER_ID)}"
    )
