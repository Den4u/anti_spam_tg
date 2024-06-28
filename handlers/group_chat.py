from string import punctuation

from aiogram import Bot, types, Router
from aiogram.filters import Command
from filters.restricted_words import restricted_words

group_router = Router()


@group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    """Проверяет является ли участник(creator-ом/administrator-ом).
    Удаляет комманду из чата."""

    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    # все данные и свойства объектов
    print(admins_list)

    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    else:
        return print("BOT!")

    # print(admins_list)


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@group_router.edited_message()
@group_router.message()
async def cleaner(message: types.Message):
    """Проверяет сообщения на запрещенные слова/удаляет."""

    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(
            f"{message.from_user.username},"
            f"в Нашем cообществе не ругаются и не ищут работу!"
            )
        await message.delete()
