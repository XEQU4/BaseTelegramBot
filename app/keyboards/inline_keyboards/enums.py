from enum import Enum


class InlineButton(str, Enum):
    START = "start"
    HELP = "help"
    SETTINGS = "settings"
    USERS = "users"
    STATS = "stats"
    BACK = "back"
