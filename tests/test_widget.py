from src.widget import get_date, mask_account_card
from tests.conftest import coll_account, coll_card, mask_account_test, mask_card_test, mask_data_test


def test_mask_account_card_1(coll_card, mask_card_test):
    for card in coll_card:
        assert mask_account_card(card) == mask_card_test


def test_mask_account_card_2(coll_account, mask_account_test):
    for account in coll_account:
        assert mask_account_card(account) == mask_account_test


def test_get_date(coll_data, mask_data_test):
    assert get_date(coll_data) == mask_data_test
