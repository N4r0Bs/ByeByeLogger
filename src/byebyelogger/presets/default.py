import pendulum

from core.repository import CustomLogger

from style.colorizer import LIGHTCYAN_EX
from style.constants import SQUARE_BRACKETS


datetime = LIGHTCYAN_EX(pendulum.now().to_datetime_string())

default = CustomLogger(order=["datetime", "level"], default_style=SQUARE_BRACKETS)

default.add(name="datetime", value=datetime)
default.add(name="level", value="INFO")

CRITICAL = default.copy()
CRITICAL.attributes["level"] = ("CRITICAL", SQUARE_BRACKETS)

ERROR = default.copy()
ERROR.attributes["level"] = ("ERROR", SQUARE_BRACKETS)

WARNING = default.copy()
WARNING.attributes["level"] = ("WARNING", SQUARE_BRACKETS)

INFO = default.copy()
INFO.attributes["level"] = (LIGHTCYAN_EX("INFO"), SQUARE_BRACKETS)

DEBUG = default.copy()
DEBUG.attributes["level"] = ("DEBUG", SQUARE_BRACKETS)
