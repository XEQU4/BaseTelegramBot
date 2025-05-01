from enum import Enum


class ReplyButton(str, Enum):
    START = "start"
    SETTINGS = "settings"
    USERS = "users"
    STATS = "stats"
    BACK = "back"
