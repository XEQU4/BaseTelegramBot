from aiogram import Router
from aiogram.types import Message

from app.dispatcher import bot
from app.utils import send_to_admins


router = Router()


@router.shutdown()
async def on_shutdown(_: Message):
    await send_to_admins(bot=bot, text="<b>🛑 The bot has been stopped!</b>")
