import logging
import re

from aiogram import Bot, types, Router, F
import aiogram
import aiogram.exceptions

from filters.type_chats import ChatTypeFilter
import exceptions as exc


# логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(
        "log_group_chat.log"), logging.StreamHandler()],
)
logger: logging.Logger = logging.getLogger(__name__)

# роутер для группового чата
group_router = Router()
group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))

# разрешённые ссылки
allowed_links: list[str] = ['https://github.com/Den4u']


@group_router.edited_message()
@group_router.message(F.text)
async def delete_message_urls_spam(message: types.Message, bot: Bot) -> None:
    """Проверяет: пользователя на права админа,
    сообщения на содержание спам ссылок, удаляет их."""

    chat_id: int = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)

    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list

    # находит все ссылки в тексте сообщения и удаляет его
    try:
        if message.from_user.id in admins_list:
            logger.info("Messages from Admin! Ok.")
            return True
        else:
            links = re.findall(
                 r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                 message.text,
                 )
            for link in links:
                if not any(link.startswith(allowed) for allowed in allowed_links):
                    logger.info(
                        "From User: %s - Spam Urls!", message.from_user.username)
                    await message.delete()

    except aiogram.exceptions.AiogramError as err:
        logger.critical("Error: %s", err)
        raise exc.DeleteMessageError("Oops, something wrong...")
