import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers.group_chat import group_router


load_dotenv()

# логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler('log_main.log'),
        logging.StreamHandler()
    ]
)
logger: logging.Logger = logging.getLogger(__name__)

# secrets
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
ADMIN_TG_ID = int(os.getenv('ADMIN_TG_ID'))


def check_tokens() -> bool:
    """Проверка доступности переменных окружения."""

    return all((BOT_TOKEN,))


async def main() -> None:
    """Основная логика работы бота."""

    # проверка на наличе токенов
    if not check_tokens():
        message = 'Need Token!'
        logger.critical(message)
        sys.exit(message)

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()

    # добавляем роутер'ы
    dp.include_router(group_router)

    # запуск событий/разрешенные методы
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logger.info("Start_ main: ")
    asyncio.run(main())
