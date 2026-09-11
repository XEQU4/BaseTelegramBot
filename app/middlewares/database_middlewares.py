from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from app.database import add_user_to_db, check_user_in_db
from app.logger import logger
from app.utils import LanguageService


class UserInDbOrNot(BaseMiddleware):
    """
    Middleware that checks whether the user exists in the database.
    If not, adds the user's ID, username, and full name.
    Also sets the user's language in FSM state (and updates DB if changed).
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        state = data.get("state")

        try:
            in_db = await check_user_in_db(user.id)
            if not in_db:
                lang = LanguageService.get_from_user(user)
                await add_user_to_db(user.id, user.username, user.full_name, lang)
                logger.info(f"New user added: {user.full_name} (@{user.username}) [{user.id}]")
        except Exception as e:  # noqa: BLE001
            logger.error(f"DB error while checking user {user.id}: {e}")

        if state:
            await LanguageService.set_to_state(state, user, enable_db_sync=False)

        return await handler(event, data)
