from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.logger import logger


class LoggerMiddleware(BaseMiddleware):
    """
    Logs incoming Telegram updates for debugging and tracking.

    Logs:
    - Chat ID
    - User ID and full name
    - Message type and text (if present)
    - Photo/video file ID and caption
    - Callback query ID, data, and message text
    """

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]  # user object
        chat = data["event_chat"]  # chat object
        message = event.message  # message object
        query = event.callback_query  # callback query object

        text = (f"[UPDATE]\n"
                f"\tChatId: {chat.id}\n"
                f"\tUserId: {user.id}\n"
                f"\tUserFullName: {user.full_name}\n"
                f"\tUpdateId: {event.update_id}")

        if message:
            text += f"\n\tMessageContentType: {message.content_type}"

            if message.text:
                text += f"\n\tMessageText: {message.text}"

            elif message.photo:
                text += (f"\n\tMessagePhotoId: {message.photo[-1].file_id}\n"
                         f"\tMessagePhotoCaption: {message.caption}")

            elif message.video:
                text += (f"\n\tMessageVideoId: {message.video.file_id}\n"
                         f"\tMessageVideoCaption: {message.caption}")

        elif query:
            text += (f"\n\tCallbackQueryId: {query.id}\n"
                     f"\tCallbackQueryData: {query.data}\n"
                     f"\tCallbackQueryText: {query.message.text}")

        logger.info(text)

        return await handler(event, data)
