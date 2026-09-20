# HelpJunior — Telegram-бот-консультант

Консультант для стажёра-разработчика, помогающий разобраться в бизнес-процессах
компании (закупки, склад, документооборот, планирование, ценообразование).
Интеграция с моделью Alice AI LLM (Yandex).

## Структура проекта

```
app/
├── config.py                     # переменные окружения и настройки
├── controllers/
│   └── bot_controller.py         # хендлеры aiogram (/start, /reset, текст)
├── models/
│   ├── history_storage.py        # история диалога по user_id (JSON)
│   └── llm_service.py            # обёртка над Alice AI LLM API
├── prompts/
│   └── system_prompt.py          # системный промпт консультанта
└── keyboards/
    └── main_kb.py                # клавиатура Telegram
run.py                             # точка входа (polling)
chat_history.json                  # хранилище истории (создаётся автоматически)
```

## Установка

1. Создать виртуальное окружение и установить зависимости:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Заполнить `.env`:
   - `BOT_TOKEN` — токен из @BotFather (создать бота с именем HelpJunior).
   - `ALICE_API_KEY`, `ALICE_FOLDER_ID` — данные доступа к Alice AI LLM.
3. Запуск: `python run.py`.

## Тестирование

Для итоговой аттестации: протестировать не менее 10 вариантов пользовательских
запросов, зафиксировать ввод, ответ консультанта, оценку (1-10) и комментарий
в таблице отчёта.
