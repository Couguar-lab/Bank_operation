import pytest

from src.masks import get_mask_account, get_mask_card_number

# from tests.conftest import coll_card, mask_account_number_answer, mask_card_number_answer


# def test_get_mask_card_number(coll_card, mask_card_number_answer):
#     for card in coll_card:
#         assert get_mask_card_number(card) == mask_card_number_answer
#
#
# def test_get_mask_account(coll_account, mask_account_number_answer):
#     for account in coll_account:
#         assert get_mask_account(account) == mask_account_number_answer
#
# @pytest.mark.parametrize("fixture_name", ["coll_card"], ids=["cards"])
# def test_get_mask_card_number(fixture_name, request):
#     """
#     Тестирует get_mask_card_number для всех элементов coll_card.
#     """
#     items = request.getfixturevalue(fixture_name)
#     mask_card_number_answer = request.getfixturevalue("mask_card_number_answer")
#     expected = mask_card_number_answer  # '7000 79** **** 6361'
#
#     for i, card in enumerate(items):
#         card_number = "".join(filter(str.isdigit, card))
#         result = get_mask_card_number(card_number)
#         assert result == expected, f"Failed for card_{i+1}: expected {expected}, got {result}"


# @pytest.mark.parametrize("index", range(10), ids=[f"card_{i+1}" for i in range(10)])
# def test_get_mask_card_number(index, request):
#     """
#     Тестирует get_mask_card_number для каждого элемента coll_card, до 10 элементов.
#     """
#     items = request.getfixturevalue("coll_card")
#     if index >= len(items):
#         pytest.skip(f"Нет карты с индексом {index}")
#
#     card = items[index]
#     card_number = "".join(filter(str.isdigit, card))  # Извлечь цифры
#     mask_card_number_answer = request.getfixturevalue("mask_card_number_answer")
#     expected = mask_card_number_answer  # '7000 79** **** 6361'
#
#     result = get_mask_card_number(card_number)
#     assert result == expected, f"Failed for card_{index+1}: expected {expected}, got {result}"


@pytest.mark.parametrize(
    "card_data, card_number_answer",
    [
        ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
        ("Visa Platinum 7000 7922 8960 6361", "7000 79** **** 6361"),
        ("Visa Platinum7000792289606361", "7000 79** **** 6361"),
        ("Visa Platinum 70007922 89606361", "7000 79** **** 6361"),
        ("Visa Platinum 7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number(card_data, card_number_answer):
    assert get_mask_card_number(card_data) == card_number_answer


@pytest.mark.parametrize(
    "account_data, account_number_answer",
    [
        ("Счет 73654108430135874305", "**4305"),
        ("Счет 7365 4108 4301 3587 4305", "**4305"),
        ("Счет73654108430135874305", "**4305"),
        ("Счет 7365410843 0135874305", "**4305"),
        ("Счет 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5", "**4305"),
    ],
)
def test_get_mask_account(account_data, account_number_answer):
    assert get_mask_account(account_data) == account_number_answer
