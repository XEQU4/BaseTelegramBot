from aiogram.fsm.storage.redis import RedisStorage

from app.redis.redis_client import redis_client

storage = RedisStorage(redis=redis_client)
