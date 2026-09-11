import asyncio
import sys

from app import errors
from app.database import db, create_tables
from app.dispatcher import bot, dp, storage
from app.handlers import on_startup, on_shutdown, connect_admin, connect_client
from app.logger import init_logger, logger
from app.middlewares import LoggerMiddleware, UserInDbOrNot
from app.redis.init_redis import redis_client
from app.scheduler.init_scheduler import start_scheduler, scheduler


async def main() -> None:
    try:
        # Initializing the Logger
        init_logger()

        # Initializing the database
        try:
            await db.create_pool()
            await create_tables()
        except BaseException:
            logger.exception("DATA BASE IS NOT CONNECTED, SO PROCESS WILL BE STOPPED!")
            raise
        logger.info("DATA BASE IS SUCCESSFUL CONNECTED!")

        # Skipping all accumulated updates
        await bot.delete_webhook(drop_pending_updates=True)

        # Adding middlewares
        dp.update.outer_middleware(UserInDbOrNot())
        dp.update.outer_middleware(LoggerMiddleware())
        logger.info("ALL MIDDLEWARES ARE CONNECTED.")

        # Connecting routers to the dispatcher
        dp.include_routers(errors.router)
        dp.include_routers(on_startup.router)
        dp.include_routers(on_shutdown.router)
        await connect_admin(dp)
        await connect_client(dp)
        logger.info("ALL ROUTERS ARE CONNECTED.")

        logger.info("BOT IS STARTED!")

        # Start the scheduler
        await start_scheduler()

        # Run events dispatching
        await dp.start_polling(bot)

    finally:
        # Cleanup: close Redis, storage, and scheduler
        await storage.close()
        await redis_client.aclose()
        if scheduler and hasattr(scheduler, "shutdown") and callable(scheduler.shutdown):
            try:
                await scheduler.shutdown()
            except Exception as e:  # noqa: BLE001
                logger.warning(f"Scheduler shutdown skipped: {e}")
        logger.info("✅ ALL RESOURCES CLEANED UP")


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.debug("BOT IS STOPPED!")
        sys.exit()

    except Exception:
        logger.critical("BOT IS STOPPED!")
        raise
