from aiogram import Dispatcher
from app.handlers.admin_handlers import commands_handlers


async def connect_admin(dp: Dispatcher) -> None:
    """
    Include all admin-related routers into the dispatcher.

    :param dp: The Dispatcher instance to register handlers to.
    """
    dp.include_router(commands_handlers.router)
