from aiogram.filters import Filter
from aiogram import types


class ChatTypeFilter(Filter):
    """Фильтр типа чата."""

    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types: list[str] = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types
