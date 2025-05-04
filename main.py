# Импорт функций маскировки из файла masks или widget
# from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# Запрос номера карты клиента и возврат замаскированного номера
# card_number = input("Введите номер карты: \n")
# print(get_mask_card_number(card_number))

# Запрос счета карты клиента и возврат замаскированного счета
# account_number = input("Введите номер счета: \n")
# print(get_mask_account(account_number))

# Запрос данных счёта или карты клиента и возврат замаскированных данных
account_card = input("Введите данные: \n")
print(mask_account_card(account_card))

# Запрос даты и возврат в удобном формате
user_date = input("Введите дату: \n")
print(get_date(user_date))
