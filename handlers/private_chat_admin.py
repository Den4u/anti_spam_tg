import logging

from aiogram import html, types, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboards.admin_kb import BASE_ADMIN_KB

from filters.type_chats import ChatTypeFilter
# , IsAdmin


# роутер для привата админ
admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]))
# , IsAdmin()


@admin_router.message(CommandStart())
async def start_cmd(message: types.Message):
    """Комманда старт."""

    logging.info(
        f'New person_guest pressed /start: {message.from_user.username} '
        f'- {html.bold(message.from_user.full_name)}.'
        )
    await message.answer(
        f"Ола! Чем могу помочь, {hbold(message.from_user.full_name)}?",
        reply_markup=BASE_ADMIN_KB)
    await message.delete()


@admin_router.message(Command("q"))
async def command_admin_handler(message: Message) -> None:
    """Обработка команды /q."""

    logging.info(
        f"New person pressed /admin: {message.from_user.username} "
        f"- {html.bold(message.from_user.full_name)}."
    )
    await message.answer("Чем я могу помочь, хозяин?")
