import os
from typing import Any, Dict
from unittest.mock import Mock, patch

import pytest
import requests
from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv()


@pytest.fixture(autouse=True)
def set_api_key():
    """Устанавливает тестовый API-ключ."""
    os.environ["EXCHANGE_API_KEY"] = "test_key"


def test_convert_to_rub_rub_currency():
    """Проверяет транзакцию в RUB."""
    transaction = {"amount": 1000.50, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 1000.50


def test_convert_to_rub_usd_currency():
    """Проверяет конвертацию USD в RUB."""
    transaction = {"amount": 50.0, "currency": "USD"}
    mock_response = {"rates": {"RUB": 90.0}}

    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        result = convert_to_rub(transaction)
        assert result == 50.0 * 90.0
        mock_get.assert_called_once_with(
            "https://api.exchangerate-api.com/v4/latest/USD", headers={"Authorization": "Bearer test_key"}, timeout=5
        )


def test_convert_to_rub_eur_currency():
    """Проверяет конвертацию EUR в RUB."""
    transaction = {"amount": 25.0, "currency": "EUR"}
    mock_response = {"rates": {"RUB": 100.0}}

    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        result = convert_to_rub(transaction)
        assert result == 25.0 * 100.0


def test_convert_to_rub_missing_amount():
    """Проверяет отсутствие amount."""
    transaction = {"currency": "RUB"}
    with pytest.raises(KeyError):
        convert_to_rub(transaction)


def test_convert_to_rub_invalid_currency():
    """Проверяет неподдерживаемую валюту."""
    transaction = {"amount": 100.0, "currency": "GBP"}
    with pytest.raises(ValueError, match="Unsupported currency: GBP"):
        convert_to_rub(transaction)


def test_convert_to_rub_api_error():
    """Проверяет ошибку API."""
    transaction = {"amount": 50.0, "currency": "USD"}
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException("Network error")
        with pytest.raises(ValueError, match="Failed to fetch exchange rate"):
            convert_to_rub(transaction)


def test_convert_to_rub_missing_api_key(monkeypatch):
    """Проверяет отсутствие API-ключа."""
    monkeypatch.delenv("EXCHANGE_API_KEY", raising=False)
    transaction = {"amount": 50.0, "currency": "USD"}
    with pytest.raises(ValueError, match="API key not found"):
        convert_to_rub(transaction)


def test_convert_to_rub_invalid_amount():
    """Проверяет некорректный amount."""
    transaction = {"amount": "invalid", "currency": "RUB"}
    with pytest.raises(ValueError, match="Amount must be a number"):
        convert_to_rub(transaction)
