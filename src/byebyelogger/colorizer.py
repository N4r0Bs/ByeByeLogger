import colorama
from colorama import Fore, Style
from typing import Any, Callable
colorama.init(autoreset=True)

class ColorDecoratorFactory:
    def __init__(self, color:str):
        self.color = color.upper()
        
        if self.color in Fore.__dict__:
            self.wrappercolor = Fore.__dict__[self.color]
        else:
            raise ValueError(f"Invalid color '{color}'. Choose a valid color from colorama.Fore.")
        
    def __call__(self, func:Callable) -> Callable:
        def wrapper(*args:Any, **kwargs:Any) -> str:
            result = func(*args, **kwargs)
            return f"{self.wrappercolor}{Style.BRIGHT}{result}"
        return wrapper
    

