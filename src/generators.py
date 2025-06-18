def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions (list): Список словарей с транзакциями.
        currency (str): Код валюты для фильтрации (например, 'USD').

    Yields:
        dict: Транзакция, где валюта соответствует заданной.
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue  # Пропускаем транзакции с некорректной структурой


def transaction_descriptions(transactions):
    """
    Генерирует описания транзакций из списка словарей.

    Args:
        transactions (list): Список словарей с транзакциями.

    Yields:
        str: Описание транзакции (поле 'description').
    """
    for transaction in transactions:
        try:
            yield transaction["description"]
        except (KeyError, TypeError):
            yield "Описание отсутствует"


def card_number_generator(start, end):
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): Начальный номер карты (от 1 до 9999999999999999).
        end (int): Конечный номер карты (от start до 9999999999999999).

    Yields:
        str: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(max(1, start), min(end + 1, 9999999999999999 + 1)):
        # Преобразуем число в строку из 16 цифр, добавляя ведущие нули
        card_number = f"{number:016d}"
        # Форматируем в группы по 4 цифры с пробелами
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
