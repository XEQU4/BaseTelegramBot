from aiogram.types import User
from aiogram.fsm.context import FSMContext
from app.config import config
from app.database import update_user_data
from app.logger import logger


class LanguageService:
    """
    A service to handle language detection, validation and persistence.

    Usage:
        lang = LanguageService.get_from_user(user)
        lang = await LanguageService.get_from_state(state, user)
    """

    @staticmethod
    def normalize(lang_code: str, fallback: str | None = None) -> str:
        """
        Normalize and validate a language code.

        :param lang_code: Raw input like 'en-US', 'ru_RU'
        :param fallback: Fallback if unsupported or missing
        :return: Valid language code from config.SUPPORTED_LANGS
        """
        fallback = fallback or config.DEFAULT_LANG
        if not lang_code:
            return fallback

        normalized = lang_code.lower().split("-")[0].split("_")[0].split(".")[0]
        return normalized if normalized in config.SUPPORTED_LANGS else fallback

    @staticmethod
    def get_from_user(user: User) -> str:
        """
        Get normalized language from Telegram user.

        :param user: Telegram User object
        :return: Validated language code
        """
        return LanguageService.normalize(getattr(user, "language_code", None))

    @staticmethod
    async def get_from_state(state: FSMContext, user: User) -> str:
        """
        Get language from FSM context or fall back to user.

        :param state: FSMContext
        :param user: Telegram User
        :return: Validated language code
        """
        data = await state.get_data()
        lang = data.get("lang")
        return lang if lang in config.SUPPORTED_LANGS else LanguageService.get_from_user(user)

    @staticmethod
    async def set_to_state(state: FSMContext, user: User, enable_db_sync: bool = True) -> str:
        """
        Normalize and store language in FSM context.
        Also updates user language in the database if changed and if enable_db_sync is True.

        :param state: FSMContext
        :param user: Telegram User
        :param enable_db_sync: We must to change the language in the Database?
        :return: Stored language code
        """
        lang = LanguageService.get_from_user(user)
        data = await state.get_data()
        saved_lang = data.get("lang")

        if saved_lang != lang:
            await state.update_data(lang=lang)

            try:
                if enable_db_sync:
                    await update_user_data(user.id, "lang", lang)
                    logger.info(f"User {user.id} language updated to '{lang}' in DB.")
            except Exception as e:  # noqa: BLE001
                logger.warning(f"Failed to update user {user.id} language in DB: {e}")

        return lang
