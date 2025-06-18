import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты для filter_by_currency
def test_filter_by_currency_usd(transactions):
    """Проверяет фильтрацию транзакций по USD."""
    filtered = list(filter_by_currency(transactions, "USD"))
    assert len(filtered) == 3
    assert [t["id"] for t in filtered] == [939719570, 142264268, 895315941]
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in filtered)


def test_filter_by_currency_rub(transactions):
    """Проверяет фильтрацию транзакций по RUB."""
    filtered = list(filter_by_currency(transactions, "RUB"))
    assert len(filtered) == 2
    assert [t["id"] for t in filtered] == [873106923, 594226727]
    assert all(t["operationAmount"]["currency"]["code"] == "RUB" for t in filtered)


def test_filter_by_currency_empty(transactions):
    """Проверяет случай, когда нет транзакций с заданной валютой."""
    filtered = list(filter_by_currency(transactions, "EUR"))
    assert filtered == []


def test_filter_by_currency_missing_keys():
    """Проверяет обработку некорректных транзакций."""
    broken_transactions = [
        {"id": 1},  # Нет operationAmount
        {"id": 2, "operationAmount": {}},  # Нет данных валюты
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},  # Корректная
    ]
    filtered = list(filter_by_currency(broken_transactions, "USD"))
    assert len(filtered) == 1
    assert filtered[0]["id"] == 3


def test_filter_by_currency_is_iterator(transactions):
    """Проверяет, что функция возвращает итератор."""
    generator = filter_by_currency(transactions, "USD")
    assert hasattr(generator, "__iter__") and hasattr(generator, "__next__")
    assert next(generator)["id"] == 939719570


# Тесты для transaction_descriptions
def test_transaction_descriptions_full_data(transactions):
    """Проверяет описания для транзакций с полными данными."""
    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected


def test_transaction_descriptions_missing_description():
    """Проверяет обработку транзакций без ключа 'description'."""
    broken_transactions = [{"id": 1}, {"id": 2, "description": "Покупка"}]  # Нет description
    descriptions = list(transaction_descriptions(broken_transactions))
    assert descriptions == ["Описание отсутствует", "Покупка"]


def test_transaction_descriptions_empty_list():
    """Проверяет обработку пустого списка."""
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


def test_transaction_descriptions_invalid_transaction():
    """Проверяет обработку некорректных транзакций."""
    broken_transactions = [None, {"description": "Покупка"}]  # Некорректный тип
    descriptions = list(transaction_descriptions(broken_transactions))
    assert descriptions == ["Описание отсутствует", "Покупка"]


def test_transaction_descriptions_is_iterator(transactions):
    """Проверяет, что функция возвращает итератор."""
    generator = transaction_descriptions(transactions)
    assert hasattr(generator, "__iter__") and hasattr(generator, "__next__")
    assert next(generator) == "Перевод организации"


# Тесты для card_number_generator
def test_card_number_format():
    """Проверяет формат номеров карт."""
    cards = list(card_number_generator(1, 3))
    assert cards == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    for card in cards:
        assert len(card) == 19  # 16 цифр + 3 пробела
        assert card[4] == " " and card[9] == " " and card[14] == " "
        assert all(part.isdigit() for part in card.split())


def test_card_number_sequence():
    """Проверяет последовательность номеров."""
    cards = list(card_number_generator(1234567890123456, 1234567890123458))
    assert cards == ["1234 5678 9012 3456", "1234 5678 9012 3457", "1234 5678 9012 3458"]


def test_minimum_start():
    """Проверяет start < 1."""
    cards = list(card_number_generator(-5, 2))
    assert cards == ["0000 0000 0000 0001", "0000 0000 0000 0002"]


def test_maximum_end():
    """Проверяет end > 9999999999999999."""
    cards = list(card_number_generator(9999999999999998, 9999999999999999 + 10))
    assert cards == ["9999 9999 9999 9998", "9999 9999 9999 9999"]


def test_start_greater_than_end():
    """Проверяет start > end."""
    cards = list(card_number_generator(10, 5))
    assert cards == []


def test_single_number():
    """Проверяет генерацию одного номера."""
    cards = list(card_number_generator(1234567890123456, 1234567890123456))
    assert cards == ["1234 5678 9012 3456"]


def test_card_number_is_iterator():
    """Проверяет, что функция возвращает итератор."""
    generator = card_number_generator(1, 3)
    assert hasattr(generator, "__iter__") and hasattr(generator, "__next__")
    assert next(generator) == "0000 0000 0000 0001"
