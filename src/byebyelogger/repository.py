from abc import ABC, abstractstaticmethod
from style import BasicLogger, LogLevel

class AbstractLoggingRepository(ABC):
    
    @abstractstaticmethod
    def DEBUG():
        pass
    
    @abstractstaticmethod
    def INFO():
        pass
    
    @abstractstaticmethod
    def WARNING():
        pass

    @abstractstaticmethod
    def ERROR():
        pass
    
    @abstractstaticmethod
    def CRITICAL():
        pass



class LogRepository(AbstractLoggingRepository):
    logger = BasicLogger()

    @staticmethod
    def DEBUG(msg: str):
        LogRepository.logger.add(LogLevel.DEBUG, msg)

    @staticmethod
    def INFO(msg: str):
        LogRepository.logger.add(LogLevel.INFO, msg)

    @staticmethod
    def WARNING(msg: str):
        LogRepository.logger.add(LogLevel.WARNING, msg)

    @staticmethod
    def ERROR(msg: str):
        LogRepository.logger.add(LogLevel.ERROR, msg)

    @staticmethod
    def CRITICAL(msg: str):
        LogRepository.logger.add(LogLevel.CRITICAL, msg)