from typing import Union

import aiosqlite
from app.logger import logger


async def execute(query: str) -> None:
    """INSERT data into database | UPDATE Database Data | DELETE Database Data."""
    async with aiosqlite.connect("database/bot_db.db") as conn:
        cur = await conn.cursor()

        try:
            await cur.execute(query)

        except aiosqlite.Error as e:
            logger.warning(f"DataBaseError - execute - [{e}] - [query: {query}]")

            await conn.rollback()

        else:
            await conn.commit()


async def fetch_one_data(query: str) -> Union[str, int, False]:
    """SELECT one element from Data Base."""
    async with aiosqlite.connect("database/bot_db.db") as conn:
        cur = await conn.cursor()

        try:
            await cur.execute(query)

        except aiosqlite.Error as e:
            logger.warning(f"DataBaseError - fetch one - [{e}] - [query: {query}]")

            return "ERROR"

        else:
            data = await cur.fetchone()

            if not data:
                return False

            return data[0]


async def fetch_one_row_data(query: str) -> Union[list, bool]:
    """SELECT row from Data Base."""
    async with aiosqlite.connect("database/bot_db.db") as conn:
        cur = await conn.cursor()

        try:
            await cur.execute(query)

        except aiosqlite.Error as e:
            logger.warning(f"DataBaseError - fetch row - [{e}] - [query: {query}]")

            return "ERROR"

        else:
            data = await cur.fetchone()

            if not data:
                return False

            return list(data)


async def fetch_all_data(query: str) -> Union[list[list], bool]:
    """SELECT all data from Data Base."""
    async with aiosqlite.connect("database/bot_db.db") as conn:
        cur = await conn.cursor()

        try:
            await cur.execute(query)

        except aiosqlite.Error as e:
            logger.warning(f"DataBaseError - fetch all - [{e}] - [query: {query}]")

            return "ERROR"

        else:
            data = await cur.fetchall()

            if not data:
                return False

            return list(data)
