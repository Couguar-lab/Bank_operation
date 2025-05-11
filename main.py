# Импорт функций маскировки из файла masks или widget
# from src.masks import get_mask_account, get_mask_card_number
#from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

# Запрос номера карты клиента и возврат замаскированного номера
# card_number = input("Введите номер карты: \n")
# print(get_mask_card_number(card_number))

# Запрос счета карты клиента и возврат замаскированного счета
# account_number = input("Введите номер счета: \n")
# print(get_mask_account(account_number))

# Запрос данных счёта или карты клиента и возврат замаскированных данных
#account_card = input("Введите данные: \n")
#print(mask_account_card(account_card))

# Запрос даты и возврат в удобном формате
#user_date = input("Введите дату: \n")
#print(get_date(user_date))

# Запрос транзакций
user_transaction = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(user_transaction))
print(sort_by_date(user_transaction))