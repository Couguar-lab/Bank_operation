# Импорт функций маскировки из файла masks
from src.masks import get_mask_account, get_mask_card_number

# Запрос номера карты клиента и возврат замаскированного номера
card_number = input("Введите номер карты: \n")
print(get_mask_card_number(card_number))

# Запрос счета карты клиента и возврат замаскированного счета
account_number = input("Введите номер счета: \n")
print(get_mask_account(account_number))
