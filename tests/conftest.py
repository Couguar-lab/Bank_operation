import pytest


# Зона для тестирования маскировки номера карты
@pytest.fixture()
def coll_card():
    return [
        "Visa Platinum 7000792289606361",
        "Visa Platinum 7000 7922 8960 6361",
        "Visa Platinum7000792289606361",
        "Visa Platinum 70007922 89606361",
        "Visa Platinum 7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1",
    ]


@pytest.fixture()
def mask_card_number_answer():
    return "7000 79** **** 6361"


@pytest.fixture()
def mask_card_answer():
    return "Visa Platinum 7000 79** **** 6361"


# Зона для тестирования маскировки номера счета
@pytest.fixture()
def coll_account():
    return [
        "Счет 73654108430135874305",
        "Счет 7365 4108 4301 3587 4305",
        "Счет73654108430135874305",
        "Счет 7365410843 0135874305",
        "Счет 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5",
    ]


@pytest.fixture()
def mask_account_number_answer():
    return "**4305"


@pytest.fixture()
def mask_account_answer():
    return "Счет **4305"


# Зона для тестирования даты
@pytest.fixture()
def coll_data():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture()
def mask_data_answer():
    return "11.03.2024"


# Зона для тестирования сортировок
@pytest.fixture()
def coll_sort():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def sort_state_executed_answer():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def sort_state_canceled_answer():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def sort_data_answer():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions():
    """Фикстура с примером транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


from pathlib import Path

# tests/conftest.py
import pytest


@pytest.fixture
def temp_log_file(tmp_path: Path) -> Path:
    """Создаёт временный файл для логов."""
    return tmp_path / "test_log.txt"
