from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

from app.config import config
from app.logger import logger


async def send_to_admins(bot: Bot, text: str) -> None:
    """
    Send a message to all admins from config.ADMINS.

    :param bot: Bot instance.
    :param text: Message text (can include HTML).
    """
    for admin_id in config.ADMINS:
        try:
            await bot.send_message(admin_id, text)
        except TelegramForbiddenError:
            logger.warning(f"Cannot send message to admin {admin_id} — bot blocked or no start.")
        except TelegramBadRequest as e:
            logger.error(f"Failed to send message to admin {admin_id}: {e}")
