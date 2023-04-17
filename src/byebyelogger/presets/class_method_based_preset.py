import inspect

from byebyelogger.core.repository import CustomLogger, LogRepository
from style.color import (
    LIGHTCYAN_EX,
    LIGHTGREEN_EX,
    LIGHTMAGENTA_EX,
    LIGHTRED_EX,
    LIGHTYELLOW_EX,
    RED,
)
from style.format import SQUARE_BRACKETS


def get_class_name_from_stack():
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        if "self" in frame.f_locals:
            name = frame.f_locals["self"].__class__.__name__
            return LIGHTGREEN_EX(name.upper())
        elif "cls" in frame.f_locals:
            name = frame.f_locals["cls"].__name__
            return LIGHTGREEN_EX(name.upper())
    return None


def get_method_name_from_stack():
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        method_name = frame.f_code.co_name
        if "self" in frame.f_locals or "cls" in frame.f_locals:
            if method_name not in [
                "<module>",
                "get_class_name_from_stack",
                "get_method_name_from_stack",
            ]:
                return LIGHTGREEN_EX(method_name.upper())
    return None


custom = CustomLogger(
    order=["class_name", "method_name", "level"], default_style=SQUARE_BRACKETS
)
custom.add(name="class_name", value=lambda: get_class_name_from_stack())
custom.add(name="method_name", value=lambda: get_method_name_from_stack())

PRESET_INFO = custom.copy()
PRESET_INFO.add(name="level", value=LIGHTCYAN_EX("INFO"))

PRESET_WARNING = custom.copy()
PRESET_WARNING.add(name="level", value=LIGHTYELLOW_EX("WARNING"))

PRESET_ERROR = custom.copy()
PRESET_ERROR.add(name="level", value=LIGHTRED_EX("ERROR"))

PRESET_DEBUG = custom.copy()
PRESET_DEBUG.add(name="level", value=LIGHTMAGENTA_EX("DEBUG"))

PRESET_CRITICAL = custom.copy()
PRESET_CRITICAL.add(name="level", value=RED("CRITICAL"))


INFO = LogRepository(PRESET_INFO)
WARNING = LogRepository(PRESET_WARNING)
ERROR = LogRepository(PRESET_ERROR)
DEBUG = LogRepository(PRESET_DEBUG)
CRITICAL = LogRepository(PRESET_CRITICAL)

__all__ = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
