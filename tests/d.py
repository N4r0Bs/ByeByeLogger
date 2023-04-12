from dataclasses import dataclass, field
from enum import Enum, auto

from style import LogStyle
from colorizer import ColorDecoratorFactory
import pendulum


class Date(Enum):
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
    
    
from enum import Enum

from enum import Enum

from enum import Enum

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __call__(self, message):
        return self.get_message(self.value, message)

    @classmethod
    def get_message(cls, value, message):
        if value == cls.DEBUG.value:
            return f"DEBUG: {message}"
        elif value == cls.INFO.value:
            return f"INFO: {message}"
        elif value == cls.WARNING.value:
            return f"WARNING: {message}"
        elif value == cls.ERROR.value:
            return f"ERROR: {message}"
        elif value == cls.CRITICAL.value:
            return f"CRITICAL: {message}"
        else:
            return "Unknown level."



@dataclass
class BaseLogger:
    
    date: Date
    time: LogTimeFormat
    level: LogLevel
    


@dataclass
class ByeByeLogger:
    logger_config: BaseLogger
