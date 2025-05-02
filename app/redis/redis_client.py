from redis.asyncio import Redis

from app.config import config

redis_client = Redis.from_url(config.REDIS_URL, decode_responses=True)
