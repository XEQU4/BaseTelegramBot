from app.config import config
from app.keyboards.reply_keyboards.enums import ReplyButton
from app.keyboards.reply_keyboards.kb_utils import create_reply_kb, get_text


class RKB:
    """
    Container class for predefined reply keyboards.

    Methods generate language-aware reply keyboards for different user roles.
    """

    @staticmethod
    def client_menu(lang: str = config.DEFAULT_LANG):
        """
        Return a reply keyboard for regular users.

        :param lang: Language code (e.g. 'en', 'ru')
        :return: ReplyKeyboardMarkup for client menu
        """
        return create_reply_kb([
            [get_text(ReplyButton.START, lang)],
            [get_text(ReplyButton.SETTINGS, lang)]
        ])

    @staticmethod
    def admin_menu(lang: str = config.DEFAULT_LANG):
        """
        Return a reply keyboard for administrators.

        :param lang: Language code (e.g. 'en', 'ru')
        :return: ReplyKeyboardMarkup for admin menu
        """
        return create_reply_kb([
            [get_text(ReplyButton.USERS, lang), get_text(ReplyButton.STATS, lang)],
            [get_text(ReplyButton.SETTINGS, lang)],
            [get_text(ReplyButton.BACK, lang)],
        ])
