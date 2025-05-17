import pytest

# Зона для тестирования маскировки номера карты
@pytest.fixture()
def coll_card():
    return ['Visa Platinum 7000792289606361',
            'Visa Platinum 7000 7922 8960 6361',
            'Visa Platinum7000792289606361',
            'Visa Platinum 70007922 89606361',
            'Visa Platinum 7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1',
            ]

@pytest.fixture()
def mask_card_number_test():
    return '7000 79** **** 6361'

@pytest.fixture()
def mask_card_test():
    return 'Visa Platinum 7000 79** **** 6361'

# Зона для тестирования маскировки номера счета
@pytest.fixture()
def coll_account():
    return ['Счет 73654108430135874305',
            'Счет 7365 4108 4301 3587 4305',
            'Счет73654108430135874305',
            'Счет 7365410843 0135874305',
            'Счет 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5']

@pytest.fixture()
def mask_account_number_test():
    return '**4305'

@pytest.fixture()
def mask_account_test():
    return 'Счет **4305'

# Зона для тестирования даты
@pytest.fixture()
def coll_data():
    return ['2024-03-11T02:26:18.671407']

@pytest.fixture()
def mask_data_test():
    return '11.03.2024'

# Зона для тестирования сортировок
@pytest.fixture()
def coll_sort():
    return [[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]]

@pytest.fixture()
def sort_state_executed_test():
    return [[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]]

@pytest.fixture()
def sort_state_canceled_test():
    return [[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]]

@pytest.fixture()
def sort_data_test():
    return [[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]]