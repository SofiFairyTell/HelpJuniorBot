import json
import os
from app.config import HISTORY_FILE, MAX_HISTORY_MESSAGES


class HistoryStorage:
    """Хранит историю диалога отдельно для каждого пользователя Telegram."""

    def __init__(self, path: str = HISTORY_FILE):
        self.path = path
        self._data = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    def get_history(self, user_id: int) -> list:
        return self._data.get(str(user_id), [])

    def add_message(self, user_id: int, role: str, text: str):
        key = str(user_id)
        history = self._data.setdefault(key, [])
        history.append({"role": role, "text": text})
        self._data[key] = history[-MAX_HISTORY_MESSAGES:]
        self._save()

    def clear(self, user_id: int):
        self._data.pop(str(user_id), None)
        self._save()
