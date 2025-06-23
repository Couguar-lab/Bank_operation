import json
from pathlib import Path
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях. Пустой список, если файл не найден,
        пустой или содержит не список.
    """
    try:
        path = Path(file_path)
        if not path.exists() or path.stat().st_size == 0:
            return []

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        return []
