from app.config import config
from app.keyboards.inline_keyboards.enums import InlineButton
from app.keyboards.inline_keyboards.ikb_utils import get_inline_text, create_inline_kb


class IKB:
    """
    Container class for predefined inline keyboards.

    Methods generate language-aware inline keyboards for different user roles.
    """

    @staticmethod
    def client_menu(lang: str = config.DEFAULT_LANG):
        """
        Return an inline keyboard for regular users.

        :param lang: Language code (e.g. 'en', 'ru')
        :return: InlineKeyboardMarkup for client menu
        """
        return create_inline_kb([
            [{"text": get_inline_text(InlineButton.HELP, lang), "callback_data": InlineButton.HELP}],
            [{"text": get_inline_text(InlineButton.SETTINGS, lang), "callback_data": InlineButton.SETTINGS}],
        ])

    @staticmethod
    def admin_menu(lang: str = config.DEFAULT_LANG):
        """
        Return an inline keyboard for administrators.

        :param lang: Language code (e.g. 'en', 'ru')
        :return: InlineKeyboardMarkup for admin menu
        """
        return create_inline_kb([
            [{"text": get_inline_text(InlineButton.USERS, lang), "callback_data": InlineButton.USERS}],
            [{"text": get_inline_text(InlineButton.STATS, lang), "callback_data": InlineButton.STATS}],
            [{"text": get_inline_text(InlineButton.BACK, lang), "callback_data": InlineButton.BACK}],
        ])
