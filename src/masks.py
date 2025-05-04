# Функция маскировки номера карты
def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты клиента"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


# Функция маскировки номера счета
def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счёта клиента"""
    return f"**{account_number[-4:]}"
