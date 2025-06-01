import pytest

from src.widget import get_date, mask_account_card
from tests.conftest import mask_data_answer



def test_get_date(coll_data, mask_data_answer):
    assert get_date(coll_data) == mask_data_answer


@pytest.mark.parametrize(
    "card_data, card_number_answer",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 70007922 89606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(card_data, card_number_answer):
    assert mask_account_card(card_data) == card_number_answer


@pytest.mark.parametrize(
    "account_data, account_number_answer",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 7365 4108 4301 3587 4305", "Счет **4305"),
        ("Счет73654108430135874305", "Счет **4305"),
        ("Счет 7365410843 0135874305", "Счет **4305"),
        ("Счет 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5", "Счет **4305"),
    ],
)
def test_mask_account_card(account_data, account_number_answer):
    assert mask_account_card(account_data) == account_number_answer
