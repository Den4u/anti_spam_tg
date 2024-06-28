import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers.group_chat import group_router
from handlers.private_chat_admin import admin_router

load_dotenv()

# logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler('log_main.log'),
        logging.StreamHandler()
    ]
)

# secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_TG_ID = int(os.getenv('ADMIN_TG_ID'))
HOST_MYSQL = os.getenv('HOST_MYSQL')
USER_MYSQL = os.getenv('USER_MYSQL')
PASSWORD_MYSQL = os.getenv('PASSWORD_MYSQL')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = int(os.getenv('DB_PORT'))


async def main() -> None:
    """Инициализируем экземпляр бота."""

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    bot.my_admins_list = []

    dp = Dispatcher()
    dp.include_router(group_router)
    dp.include_router(admin_router)

    # проброс в каждый Хэндлер!!! посмотреть настройки под каждый!
    # dp.update.middleware(DataBaseSession(session_pool=session_maker))

    # delete_webhook
    await bot.delete_webhook(drop_pending_updates=True)

    # the run events dispatching/allowed_updates: разрешенные методы
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
