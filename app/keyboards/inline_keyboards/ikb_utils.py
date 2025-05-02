from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.keyboards.inline_keyboards.texts import INLINE_TEXTS
from app.config import config


def get_inline_text(code: str, lang: str) -> str:
    return INLINE_TEXTS.get(lang, INLINE_TEXTS[config.DEFAULT_LANG]).get(code, str(code))


def create_inline_kb(buttons: list[list[dict]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(**btn) for btn in row]
            for row in buttons
        ]
    )
