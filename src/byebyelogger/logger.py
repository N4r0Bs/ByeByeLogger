from dataclasses import dataclass, field
from typing import Callable, Dict, List, Protocol, Tuple, Union

from style.color import (
    LIGHTCYAN_EX,
    LIGHTMAGENTA_EX,
    LIGHTRED_EX,
    LIGHTYELLOW_EX,
    RED,
)
from style.format import SQUARE_BRACKETS


@dataclass
class LoggerConfiguration:
    attributes: Dict[str, Tuple[Union[str, Callable], str]] = field(
        default_factory=dict
    )
    order: List[str] = field(default_factory=list)
    separator: str = " - "
    default_style: str = ""

    def __post_init__(self):
        if self.default_style:
            self.set_style(self.default_style)

    def add(self, value: Union[str, Callable], style: str = None):
        name = str(value)
        if style is None:
            style = SQUARE_BRACKETS  # setzt automatisch Square Brackets als Style
        self.attributes[name] = (value, style)
        self.order.append(name)

    def set_order(self, order: List[str]):
        self.order = order

    def set_style(self, style: str):
        self.default_style = style

    def apply_style(self, style: str, text: str):
        return style.format(text)

    def log(self):
        formatted_attributes = []
        for attr in self.order:
            value, style = self.attributes[attr]
            if callable(value):
                value = value()
            formatted_value = self.apply_style(
                style, str(value)
            )  # konvertiert Wert zu String
            formatted_attributes.append(formatted_value)

        log_entry = self.separator.join(formatted_attributes)
        print(log_entry, end=" ")


class Preset(Protocol):
    def log(self):
        pass


class Logger:
    def __init__(self, logging: Preset):
        self.logging = logging

    def log(self, msg: str):
        self.logging.log()
        print(msg)


def create_logger(level_color: str, level_name: str, style: str = None) -> Logger:
    configuration = LoggerConfiguration()
    configuration.add(level_color(level_name), style)
    return Logger(configuration)


__all__ =  ["create_logger"]