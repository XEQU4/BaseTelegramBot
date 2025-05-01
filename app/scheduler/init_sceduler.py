from datetime import datetime, timedelta

import pytz
from aiogram import Bot
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator

from app.dispatcher import bot
from app.logger import logger
from app.redis.init_redis import redis_client

jobstores = {
    "default": RedisJobStore(redis=redis_client)
}

# Scheduler + DI
scheduler = ContextSchedulerDecorator(AsyncIOScheduler(jobstores=jobstores))
scheduler.ctx.add_instance(bot, declared_class=Bot)


async def say_hello() -> None:
    logger.info("👋 APScheduler test task executed.")


async def start_scheduler() -> None:
    """
    Start APScheduler and add a test task.
    """
    try:
        scheduler.start()

        moscow_tz = pytz.timezone("Europe/Moscow")
        run_date = datetime.now(tz=moscow_tz) + timedelta(seconds=1)

        scheduler.add_job(
            say_hello,
            trigger="date",
            run_date=run_date,
            id="startup_test_task",
            name="Test job: say_hello once after start",
            replace_existing=True,
        )

        logger.info("APSCHEDULER STARTED SUCCESSFULLY!")

    except Exception as e:
        logger.critical(f"FAILED TO START APSCHEDULER: {e}")
        raise
