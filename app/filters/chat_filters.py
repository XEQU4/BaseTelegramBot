from typing import Union

from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message
from app.config import config


class IsAdmin(Filter):
    """Checking if a user is an administrator."""

    def __init__(self) -> None:
        pass

    async def __call__(self, query_or_message: Union[Message, CallbackQuery]) -> bool:
        return query_or_message.from_user.id in config.ADMINS


class IsClient(Filter):
    """Checking if a user is an administrator."""

    def __init__(self) -> None:
        pass

    async def __call__(self, query_or_message: Union[Message, CallbackQuery]) -> bool:
        return query_or_message.from_user.id not in config.ADMINS
