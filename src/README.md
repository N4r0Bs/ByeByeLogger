# ByeByeLogger

### Oh, great! Another logging package, because obviously, we need more of those, right? Well, let me introduce you to ByeByeLogger, the one that's going to make you say goodbye to your current logger (whether you like it or not).


# Installation
To get this totally groundbreaking package, just do the usual `pip` dance:
```bash
pip install byebyelogger
```
# Features
- Create simple loggers with just a few lines of code
- Customize log output with colors, formats, and callables
- Easily integrate with existing codebases

# Example Usage
## Simple Logger
Create a simple logger with a custom color and level:
```python
from byebyelogger import single_logger
from byebyelogger.style.color import RED
from byebyelogger.style.format import SQUARE_BRACKETS

logger = single_logger(RED, "INFO", SQUARE_BRACKETS)
logger.log("This is an example message.")
```
Output:

```bash
[INFO] This is an example message.
```
## Nested Logger
```python
from byebyelogger import nested_logger
from byebyelogger.style.color import LIGHTCYAN_EX
from byebyelogger.style.format import SQUARE_BRACKETS
from datetime import datetime

def timestamp_func():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

components = [
    (timestamp_func, SQUARE_BRACKETS),
    ("SQLITE", SQUARE_BRACKETS),
    (LIGHTCYAN_EX("INFO"), None),
]

logger = nested_logger(components)
logger.log("This is an example message.")
```
Output:
```bash
[2023-01-01 01:00:00] [SQLITE] INFO This is an example message.
```
# Documentation
For more detailed information on how to use `ByeByeLogger`, please refer to the inline documentation in the package files:

- `logger.py`
- `core/configuration.py`
- `core/stack_info.py`
- `style/color.py`
- `style/format.py`
# License
ByeByeLogger is released under the MIT License.

# Contributing
We welcome contributions to ByeByeLogger! If you'd like to contribute, please fork the repository and submit a pull request. We'll review your changes and merge them in if everything looks good.



