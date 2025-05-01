import os
from dotenv import load_dotenv


class Config:
    """
    Loads environment variables and stores bot configuration.

    Attributes:
        ADMINS (list[int]): List of admin user IDs (split by "/").
        BOT_TOKEN (str): Telegram bot token.
        REDIS_URL (str): Redis connection string.
    """

    def __init__(self):
        load_dotenv()

        admins_raw = os.getenv("ADMINS", "")
        self.ADMINS = list(map(int, admins_raw.split("/"))) if admins_raw else []

        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.REDIS_URL = os.getenv("REDIS_URL")

        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is missing in .env")

        if not self.REDIS_URL:
            raise ValueError("REDIS_URL is missing in .env")


config: Config = Config()