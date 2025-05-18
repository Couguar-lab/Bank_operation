from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import coll_card, mask_account_number_test, mask_card_number_test


def test_get_mask_card_number(coll_card, mask_card_number_test):
    for card in coll_card:
        assert get_mask_card_number(card) == mask_card_number_test


def test_get_mask_account(coll_account, mask_account_number_test):
    for account in coll_account:
        assert get_mask_account(account) == mask_account_number_test
