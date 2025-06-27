import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Настройка логгера
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях. Пустой список, если файл не найден,
        пустой или содержит не список.
    """
    logger.info(f"Загрузка транзакций из {file_path}")
    try:
        path = Path(file_path)
        if not path.exists():
            logger.error(f"Файл не найден: {file_path}")
            return []
        if path.stat().st_size == 0:
            logger.warning(f"В файле нет данных: {file_path}")
            return []

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.error(f"Файл не содержит список: {file_path}")
                return []
            logger.info(f"Успешная загрузка {len(data)} транзакций из {file_path}")
            return data
    except json.JSONDecodeError as e:
        logger.error(f"Недопустимый формат JSON в {file_path}: {str(e)}")
        return []
    except PermissionError as e:
        logger.error(f"Отсутствует доступ к {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке {file_path}: {type(e).__name__}: {str(e)}")
        return []
