import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore


async def say_hi():
    print("hi")


async def main():
    scheduler = AsyncIOScheduler(
        jobstores={"default": RedisJobStore(db=5, host="localhost", port=6379)}
    )

    scheduler.start()
    scheduler.add_job(say_hi, "interval", seconds=5)  # ✅ теперь можно

    await asyncio.sleep(15)  # дай задаче поработать

asyncio.run(main())
