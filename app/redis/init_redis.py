from redis.asyncio import Redis  # Asynchronous Redis client
from aiogram.fsm.storage.redis import RedisStorage

from app.config import config

redis_client = Redis.from_url(url=config.REDIS_URL, decode_responses=True)
storage = RedisStorage(redis=redis_client)
