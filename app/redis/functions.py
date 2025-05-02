from app.redis.redis_client import redis_client


async def set_redis_value(key: str, value: str, timeout: int = None) -> None:
    """
    Set or update a key in Redis.

    :param key: The key name.
    :param value: The value to store.
    :param timeout: Optional expiration time in seconds.
    """
    await redis_client.set(name=key, value=value, ex=timeout)


async def delete_redis_keys(keys: list[str]) -> None:
    """
    Delete one or more keys from Redis.

    :param keys: A list of keys to delete.
    """
    await redis_client.delete(*keys)


async def get_redis_value(keys: list[str] | str) -> list[str] | str | None:
    """
    Retrieve one or more values from Redis.

    :param keys: A single key (str) or list of keys (list[str]).
    :return:
        - If a single key is provided:
            Returns the value as a string, or None if the key does not exist.
        - If multiple keys are provided:
            Returns a list of values in the same order as the keys.
            If at least one key exists, the list may contain `None` for missing keys.
            If all keys are missing, returns None.

    Example:
        >> await get_redis_value("user:1")
        "Alice"

        >> await get_redis_value(["user:1", "user:2"])
        ["Alice", "Bob"]

        >> await get_redis_value(["user:1", "missing:2"])
        ["Alice", None]

        >> await get_redis_value(["missing:1", "missing:2"])
        None
    """
    if isinstance(keys, list):
        values = await redis_client.mget(*keys)
        return values if any(v is not None for v in values) else None
    else:
        value = await redis_client.get(keys)
        return value if value is not None else None
