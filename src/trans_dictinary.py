import re
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по строке поиска в описании с использованием регулярных выражений.

    Args:
        data: Список словарей с данными о транзакциях.
        search: Строка для поиска в поле 'description'.

    Returns:
        Список словарей с транзакциями, где описание содержит строку поиска (без учёта регистра).
    """
    if not search:
        return data
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(str(transaction.get("description", "")))]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество транзакций для каждой категории.

    Args:
        data: Список словарей с данными о транзакциях.
        categories: Список категорий для подсчёта.

    Returns:
        Словарь, где ключи — категории, значения — количество транзакций в каждой категории.
    """
    result = {category: 0 for category in categories}
    for transaction in data:
        description = str(transaction.get("description", ""))
        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1
    return result
