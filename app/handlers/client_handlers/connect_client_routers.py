from aiogram import Dispatcher
from app.handlers.client_handlers import commands_handlers


async def connect_client(dp: Dispatcher) -> None:
    """
    Include all client-related routers into the dispatcher.

    :param dp: The Dispatcher instance to register handlers to.
    """
    dp.include_routers(commands_handlers.router)
