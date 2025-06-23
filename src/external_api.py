import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, используя текущий курс валют.

    Args:
        transaction: Словарь с данными транзакции, содержащий 'amount' и 'currency'.

    Returns:
        Сумма в рублях (float).

    Raises:
        KeyError: Если в транзакции отсутствуют 'amount' или 'currency'.
        ValueError: Если валюта не поддерживается или API недоступен.
    """
    amount = transaction["amount"]
    currency = transaction["currency"].upper()

    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")

    if currency == "RUB":
        return float(amount)

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Unsupported currency: {currency}")

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables")

    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        rate = data["rates"].get("RUB")
        if not rate:
            raise ValueError("RUB rate not found in API response")

        return float(amount) * rate
    except (requests.RequestException, KeyError) as e:
        raise ValueError(f"Failed to fetch exchange rate: {str(e)}")
