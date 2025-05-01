import sys

import aiosqlite
from aiosqlite import Cursor
from app.logger import logger


async def init_db() -> None:
    """
    Create tables in the database.

    ID—telegram user_id
    username—user @user_name
    fullname—user full_name
    lang—user language
    """
    try:
        async with aiosqlite.connect("app/database/bot_db.db") as conn:
            cur: Cursor = await conn.cursor()
            await cur.execute("""
                              CREATE TABLE IF NOT EXISTS user(
                                  id VARCHAR(12) PRIMARY KEY,
                                  username VARCHAR(32),
                                  fullname TEXT,
                                  lang VARCHAR(15)
                              )
                              """)

            await conn.commit()

    except aiosqlite.Error as e:
        logger.exception(f"DATA BASE IS NOT CONNECTED, SO PROCESS WILL BE STOPPED!\nError: {e}")
        sys.exit()
