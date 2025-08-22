import logging
from typing import Any


def init_logging(level: str = "INFO") -> None:
    root = logging.getLogger()
    root.handlers.clear()

    fmt = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    formatter = logging.Formatter(fmt)

    root.setLevel(get_level(level))

    h = logging.StreamHandler()
    h.setFormatter(formatter)
    h.setLevel(logging.NOTSET)  # let the logger decide
    root.addHandler(h)


def get_level(str_level: str) -> Any:
    """Get logging level

    :param str_level: string representation of logging level (e.g. DEBUG, INFO, ERROR, ...)
    :return: logging level as attribute of logging package
    """
    if not hasattr(logging, str_level):
        raise ValueError(f"Invalid logging level '{str_level}' in configuration")
    return getattr(logging, str_level)
