from typing import Iterable

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.config import config
from app.keyboards.reply_keyboards.texts import BUTTON_TEXTS


def create_reply_kb(buttons: Iterable[Iterable[str]], resize: bool = True) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=resize,
        keyboard=[[KeyboardButton(text=btn) for btn in row] for row in buttons]
    )


def get_text(code: str, lang: str) -> str:
    return BUTTON_TEXTS.get(lang, BUTTON_TEXTS[config.DEFAULT_LANG]).get(code, str(code))
