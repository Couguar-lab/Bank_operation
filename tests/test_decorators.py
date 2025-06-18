# tests/test_decorators.py
import logging  # Добавляем импорт logging
import os
from typing import Optional

import pytest

from src.decorators import log


@pytest.fixture
def temp_log_file(tmp_path):
    """Создаёт временный файл для логов."""
    return tmp_path / "test_log.txt"


def read_log_file(filepath: str) -> list[str]:
    """Читает строки из лог-файла."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def test_log_success_console(caplog):
    """Проверяет логирование успешного выполнения в консоль."""
    caplog.set_level(logging.INFO)

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5

    log_messages = [record.message for record in caplog.records]
    assert log_messages == ["add ok", "add result: 5"]


def test_log_success_file(temp_log_file):
    """Проверяет логирование успешного выполнения в файл."""

    @log(filename=str(temp_log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(4, 5)
    assert result == 20

    logs = read_log_file(str(temp_log_file))
    assert logs == ["multiply ok", "multiply result: 20"]


def test_log_error_console(caplog):
    """Проверяет логирование ошибки в консоль."""
    caplog.set_level(logging.ERROR)

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    log_messages = [record.message for record in caplog.records]
    assert any("divide error: ZeroDivisionError. Inputs: (10, 0), {}" in msg for msg in log_messages)


def test_log_error_file(temp_log_file):
    """Проверяет логирование ошибки в файл."""

    @log(filename=str(temp_log_file))
    def faulty_func(x: int) -> int:
        raise ValueError("Тестовая ошибка")

    with pytest.raises(ValueError, match="Тестовая ошибка"):
        faulty_func(42)

    logs = read_log_file(str(temp_log_file))
    assert any("faulty_func error: ValueError. Inputs: (42,), {}" in line for line in logs)


def test_log_with_kwargs(temp_log_file):
    """Проверяет логирование с именованными аргументами."""

    @log(filename=str(temp_log_file))
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    assert result == "Hi, Alice!"

    logs = read_log_file
