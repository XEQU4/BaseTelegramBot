from app.locales.texts import MESSAGES


def t(key: str, lang: str = "en", **kwargs) -> str:
    """
    Get translated text with optional formatting.

    :param key: Text key, like 'greet_admin'
    :param lang: Language code ('en', 'ru', ...)
    :param kwargs: Variables for formatting like {name=...}
    :return: Translated and formatted string
    """
    template = MESSAGES.get(lang, MESSAGES["en"]).get(key, key)
    return template.format(**kwargs)
