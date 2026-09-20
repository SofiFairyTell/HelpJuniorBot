from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.models.history_storage import HistoryStorage
from app.models.llm_service import LLMService
from app.keyboards.main_kb import main_menu_kb

router = Router()
history_storage = HistoryStorage()
llm_service = LLMService()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я HelpJunior — консультант для стажёров-разработчиков.\n"
        "Спрашивай про бизнес-процессы компании: закупки, склад, документооборот, "
        "планирование, ценообразование. Помогу разобраться простыми словами.",
        reply_markup=main_menu_kb,
    )


@router.message(Command("reset"))
async def cmd_reset(message: Message):
    history_storage.clear(message.from_user.id)
    await message.answer("История диалога очищена.")


@router.message(F.text == "Очистить историю диалога")
async def btn_reset(message: Message):
    await cmd_reset(message)


@router.message(F.text)
async def handle_question(message: Message):
    user_id = message.from_user.id
    user_text = message.text

    await message.bot.send_chat_action(message.chat.id, "typing")

    history = history_storage.get_history(user_id)
    answer = llm_service.ask(history, user_text)

    history_storage.add_message(user_id, "user", user_text)
    history_storage.add_message(user_id, "assistant", answer)

    await message.answer(answer)
