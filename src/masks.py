# Функция маскировки номера карты
def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты клиента"""
    card_number_clear = "".join(filter(str.isdigit, card_number))
    return f"{card_number_clear[0:4]} {card_number_clear[4:6]}** **** {card_number_clear[-4:]}"


# Функция маскировки номера счета
def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счёта клиента"""
    account_number_clear = "".join(filter(str.isdigit, account_number))
    return f"**{account_number_clear[-4:]}"
