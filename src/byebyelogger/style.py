import pendulum

from enum import Enum
from dataclasses import dataclass


class LogStyle(Enum):
    DEFAULT = "[::{}::]"
    PARENTHESES = "({})"
    SQUARE_BRACKETS = "[{}]"
    CURLY_BRACKETS = "{{{}}}"
    DOUBLE_QUOTES = "\"{}\""
    SINGLE_QUOTES = "\'{}\'"
    TRIANGLE_BRACKETS = "<{}>"
    TAGS = "<!-- {} -->"
    ANGLED_BRACKETS = "< {} >"
    DOUBLE_COLONS = "::{}::"
    STARRED = "/* {} */"
    DASHES = "--- {} ---"
    UNDERSCORES = "___ {} ___"
    ARROW = "-> {}"
    DOUBLE_ARROW = "->> {}"
    PIPE = "|{}|"
    TILDE = "~+~{}"
    PLUS = "+++ {} +++"
    ASTERISKS = "*** {} ***"
    QUESTION_MARK = "? {} ?"
    EXCLAMATION_MARK = "! {} !"
    
    def apply(self, text):
        return self.value.format(text)


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __str__(self):
        return self.value
    
@dataclass
class BaseLoggerPreset:
    datetime_style: LogStyle
    level_style: LogStyle
    message_style: LogStyle

    def add(self, log_level: LogLevel, msg: str):
        datetime = self.datetime_style.apply(pendulum.now().to_datetime_string())
        level = self.level_style.apply(str(log_level))
        message = self.message_style.apply(msg)
        log_entry = f"{datetime} - {level} - {message}"
        print(log_entry)
        

