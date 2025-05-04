# Импорт функций маскировки из файла masks
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскирует номер счета или карты в зависимости от предоставленных данных"""
    number_account_card = "".join(filter(str.isdigit, account_card))
    if len(number_account_card) > 16:
        return f"{account_card[:-21]} {get_mask_account(number_account_card)}"
    else:
        return f"{account_card[:-17]} {get_mask_card_number(number_account_card)}"


# Функция преобразования даты
def get_date(user_date: str) -> str:
    """Функция преобразовывает и выводит получаемую дату в формате ДД.ММ.ГГГГ"""
    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"
