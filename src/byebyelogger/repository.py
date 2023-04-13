from abc import ABC, abstractmethod
from typing import Protocol

from style import LogLevel, BaseLoggerPreset, LogStyle

class AbstractLoggingRepository(ABC):
    
    @abstractmethod
    def DEBUG():
        pass
    
    @abstractmethod
    def INFO():
        pass
    
    @abstractmethod
    def WARNING():
        pass

    @abstractmethod
    def ERROR():
        pass
    
    @abstractmethod
    def CRITICAL():
        pass


class LogMessageProcessor(Protocol):
    def add(self, log_level: LogLevel, msg:str):
        pass


class LogRepository(AbstractLoggingRepository):

    def __init__(self, logging: LogMessageProcessor):
        self.logging = logging

    def DEBUG(self, msg: str):
        self.logging.add(LogLevel.DEBUG, msg)

    def INFO(self, msg: str):
        self.logging.add(LogLevel.INFO, msg)

    def WARNING(self, msg: str):
        self.logging.add(LogLevel.WARNING, msg)

    def ERROR(self, msg: str):
        self.logging.add(LogLevel.ERROR, msg)

    def CRITICAL(self, msg: str):
        self.logging.add(LogLevel.CRITICAL, msg)


simple = BaseLoggerPreset(datetime_style=LogStyle.SQUARE_BRACKETS, level_style=LogStyle.SQUARE_BRACKETS, message_style=LogStyle.SQUARE_BRACKETS)
