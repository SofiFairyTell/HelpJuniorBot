from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как устроен процесс закупок?")],
        [KeyboardButton(text="Очистить историю диалога")],
    ],
    resize_keyboard=True,
)
