from asyncpg import exceptions

from app.database import db
from app.logger import logger


@logger.catch
async def create_tables() -> None:
    """
    Creating tables in the database.
    """
    pool = await db.get_pool()

    async with pool.acquire() as conn:
        try:
            async with conn.transaction():
                query = """
                        CREATE TABLE IF NOT EXISTS user (
                            id BIGINT PRIMARY KEY,
                            username VARCHAR(32),
                            fullname TEXT,
                            lang VARCHAR(15)
                        )
                        """
                await conn.execute(query)

        except exceptions.PostgresError as err:
            logger.exception(f"TABLES ARE NOT CREATED, SO THE BOT IS STOPPED! ERROR - {err}")
            raise err

        else:
            logger.info("ALL TABLES HAVE BEEN CREATED IN THE DATABASE!")
