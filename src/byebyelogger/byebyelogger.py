from dataclasses import dataclass, field
from enum import Enum

from colorizer import ColorDecoratorFactory

import pendulum

class DateEnumaration(Enum):
    DATE = f"{pendulum.now().to_date_string()}"
    DATETIME = f"{pendulum.now().to_day_datetime_string()}"
    MONTH_DAY_YEAR = f"{pendulum.now().to_formatted_date_string()}"
    COOKIE_STRING = f"{pendulum.now().to_cookie_string()}"
    TIME = f"{pendulum.now().to_time_string()}"
    
    
    def __str__(self):
        return self.value



class ByeByeLogger:
    pass

