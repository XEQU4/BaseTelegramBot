from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import config
from app.redis.init_redis import storage

# Initialize Bot instance with a default parse mode, which will be passed to all API calls.
bot = Bot(config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Dispatcher with Redis-based FSM storage (for persistent state across restarts)
dp = Dispatcher(storage=storage)
