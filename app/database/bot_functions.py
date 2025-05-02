from app.database import db
from app.logger import logger


@logger.catch
async def get_users_from_db(user_id: str | int = None) -> list[dict] | dict | None:
    """
    [\n
        {'id': 1, 'username': 'john_doe', 'fullname': 'John Doe', 'lang': 'en'},\n
        {'id': 2, 'username': 'jane_smith', 'fullname': 'Jane Smith', 'lang': 'fr'},\n
        {'id': 3, 'username': 'alisa_vladimir', 'fullname': 'Alisa Vladimir', 'lang': 'ru'}]\n
        {'id': 4, 'username': 'max_john', 'fullname': 'Max John', 'lang': 'en-US'}]\n
        . . .\n
    ]
    """
    pool = await db.get_pool()

    if user_id:
        user_id = int(user_id)
        query = """
        SELECT * FROM users WHERE user_id = $1
        """
        async with pool.acquire() as conn:
            async with conn.transaction():
                record = await conn.fetchrow(query,
                                             user_id)

        return dict(record) if record else None

    else:
        query = """
        SELECT * FROM users
        """
        async with pool.acquire() as conn:
            async with conn.transaction():
                records = await conn.fetch(query)

        return [dict(chat_record) for chat_record in records] if records else None


@logger.catch
async def add_user_to_db(
        user_id: int | str, username: str, fullname: str, lang: str
) -> None:
    """Add new user to Data Base."""
    user_id = int(user_id)
    user_ids = [user['id'] for user in await get_users_from_db()]

    if user_id in user_ids:
        return

    query = """
    INSERT INTO user (
        id, username, fullname, lang
    )
    VALUES (
        $1, $2, $3, $4
    )
    """  # noqa: S608

    pool = await db.get_pool()

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(query,
                               user_id,
                               username,
                               fullname,
                               lang)


@logger.catch
async def update_user_data(
        user_id: int | str, column: str, new_data: int | str
) -> int | None:
    """Update user data in Data Base. If user not in Database, return user_id."""
    user_id = int(user_id)
    if await get_users_from_db(user_id) is None:
        return int(user_id)

    query = """
            UPDATE user
            SET $1 = $2
            WHERE id = $3
            """

    pool = await db.get_pool()

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(query,
                               column,
                               new_data,
                               user_id)
    return None


@logger.catch
async def check_user_in_db(user_id: int) -> bool:
    """Check user in Data Base."""
    user_id = int(user_id)
    user = await get_users_from_db(user_id)

    if user:
        return True
    return False


@logger.catch
async def get_lang_from_db(user_id: int | str) -> str:
    """Get user's lang from db."""
    user_id = int(user_id)
    user = await get_users_from_db(user_id)

    return user['lang']
