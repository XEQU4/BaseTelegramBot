from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from app.database.bot_functions import (
    add_user_to_db,
    check_user_in_db,
)
from app.logger import logger


class UserInDbOrNot(BaseMiddleware):
    """
    Middleware that checks whether the user exists in the database.
    If not, adds the user's ID, username, and full name.
    Also sets the user's language in FSM state if available.
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]  # aiogram.User
        state = data.get("state")       # FSMContext, is exists
        lang_code = getattr(user, "language_code", "en")  # user's language from telegram

        try:
            in_db = await check_user_in_db(user.id)
            if not in_db:
                await add_user_to_db(user.id, user.username, user.full_name, lang_code)
                logger.info(f"New user added: {user.full_name} (@{user.username}) [{user.id}]")
        except Exception as e:
            logger.warning(f"DB error while checking user {user.id}: {e}")

        # Initializing the language of the user (if FSM is exists)
        if state:
            supported_langs = {"en", "ru"}
            lang = lang_code if lang_code in supported_langs else "en"
            await state.update_data(lang=lang)

        return await handler(event, data)
