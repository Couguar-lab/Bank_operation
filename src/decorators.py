# src/decorators.py
import logging
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

# Типы для параметров и возвращаемого значения
P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для логирования выполнения функции.

    Args:
        filename: Имя файла для записи логов. Если None, логи выводятся в консоль.

    Returns:
        Декорированная функция с логированием.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Настройка логирования
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            # Очищаем обработчики, чтобы избежать дублирования
            while logger.handlers:
                logger.handlers.pop()

            # Выбор обработчика: файл или консоль
            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler()
            formatter = logging.Formatter("%(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                logger.info(f"{func.__name__} ok")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} result: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                handler.close()
                logger.removeHandler(handler)

        return wrapper

    return decorator
