# ByeByeLogger

___Oh, great! Another logging package, because obviously, we need more of those, right? Well, let me introduce you to ByeByeLogger, the one that's going to make you say goodbye to your current logger (whether you like it or not).___
_- by bl0ckm0n_

<img src="https://pixabay.com/get/g6103bb292404fa7ac48251d7423809a84de9bb4c0170d595a35f272ae6449c21bafcf15403e6118fa096c262c674efa6f56d4170a5d3c8fa63347a87dd311748acc9233e5626ada025ba5ad1a25ded4f_1280.jpg"/>  

_Bild von <a href="https://pixabay.com/de/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3258939">Gerd Altmann</a> auf <a href="https://pixabay.com/de//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3258939">Pixabay</a>._

<br>

## Installation

To get this totally groundbreaking package, just do the usual `pip` dance:

```bash
pip install byebyelogger
```

<br>

## Features

- Create _simple_ loggers with just a few lines of code

- _Customize_ log output with colors, formats, and callables

- _Easily_ integrate with existing codebases

<br>

## How to Usage

The Code examples below show possible uses of ByeByeLogger.

<br>

### _Simple Logger_

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

<br>

### _Nested Logger_
```python
from byebyelogger import nested_logger
from byebyelogger.style.color import LIGHTCYAN_EX
from byebyelogger.style.format import SQUARE_BRACKETS
from datetime import datetime

def timestamp_func():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

components = [
    (lambda:timestamp_func(), SQUARE_BRACKETS),
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

<br>

## Documentation

For more detailed information on how to use `ByeByeLogger`, please refer to the inline documentation in the package files:

- `logger.py`

- `core/configuration.py`

- `core/stack_info.py`

- `style/color.py`

- `style/format.py`

<br>

## Contributing & License

We welcome contributions to ByeByeLogger! If you'd like to contribute, please fork the repository and submit a pull request. We'll review your changes and merge them in if everything looks good. ByeByeLogger is released under the MIT License.
