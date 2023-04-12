import pendulum

from enum import Enum

class LogDateFormat(Enum):
    DATE_ISO = "YYYY-MM-DD"
    DATE_DMY = "DD.MM.YYYY"
    DATE_MDY = "MM/DD/YYYY"
    DATE_LONG = "dddd, DD MMMM YYYY"
     
    def __str__(self):
        return pendulum.now().format(self.value)

class LogTimeFormat(Enum):
    TIME_24 = "HH:mm:ss"
    TIME_24_HM = "HH:mm"  # Added HH:MM format
    TIME_12 = "hh:mm:ss A"
    UNIX_TIMESTAMP = "X"
     
    def __str__(self):
        return pendulum.now().format(self.value)
    

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
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.value.format(result)
        return wrapper


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __str__(self):
        return self.value


class BasicLogger:
    def __init__(self, date_format: LogDateFormat = LogDateFormat.DATE_ISO,
                 time_format: LogTimeFormat = LogTimeFormat.TIME_24_HM,
                 level_format: LogLevel = "{}",
                 message_format: str = "{}"):
        self.date_format = date_format
        self.time_format = time_format
        self.level_format = level_format
        self.message_format = message_format

    @LogStyle.SQUARE_BRACKETS
    def format_date(self):
        return str(self.date_format)
    
    @LogStyle.SQUARE_BRACKETS
    def format_time(self):
        return str(self.time_format)

    @LogStyle.SQUARE_BRACKETS
    def format_level(self, level: str):
        return str(self.level_format).format(level)

    @LogStyle.DOUBLE_ARROW
    def format_message(self, message: str):
        return str(self.message_format).format(message)

    def add(self, level: LogLevel, message: str):
        date_str = self.format_date()
        time_str = self.format_time()
        level_str = self.format_level(level.value)
        message_str = self.format_message(message)
        log_str = f"{date_str} : {time_str} - {level_str} - {message_str}"
        print(log_str)
