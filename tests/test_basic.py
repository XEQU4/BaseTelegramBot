import pytest
from aiogram import Bot


@pytest.mark.asyncio
async def test_bot_token_loading():
    from app.config import config

    assert config.BOT_TOKEN, "BOT_TOKEN should not be empty"
    bot = Bot(token=config.BOT_TOKEN)
    assert bot.token == config.BOT_TOKEN
