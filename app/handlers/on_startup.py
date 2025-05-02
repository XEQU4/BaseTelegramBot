from aiogram import Router

from app.dispatcher import bot
from app.utils import send_to_admins

router = Router()


@router.startup()
async def on_startup():
    await send_to_admins(bot=bot, text="<b>✅ The bot has been successfully started!</b>")
