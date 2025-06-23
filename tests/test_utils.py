import json
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions


def test_load_transactions_valid_json(tmp_path):
    """Проверяет чтение корректного JSON-файла."""
    data = [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 50.0, "currency": "USD"}]
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == data


def test_load_transactions_empty_file(tmp_path):
    """Проверяет пустой файл."""
    file_path = tmp_path / "empty.json"
    file_path.touch()

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_nonexistent_file():
    """Проверяет несуществующий файл."""
    result = load_transactions("nonexistent.json")
    assert result == []


def test_load_transactions_invalid_json(tmp_path):
    """Проверяет некорректный JSON."""
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid}", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_non_list(tmp_path):
    """Проверяет JSON с не списком."""
    data = {"key": "value"}
    file_path = tmp_path / "non_list.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []
