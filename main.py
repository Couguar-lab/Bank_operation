from typing import Any, Dict, List

import pandas as pd

from src.processing import filter_by_state, sort_by_date
from src.trans_dictinary import process_bank_operations, process_bank_search
from src.trans_reader import read_trans_from_csv, read_trans_from_xls
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная логика программы для работы с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    file_path = ""
    transactions: List[Dict[str, Any]] = []

    # Выбор источника данных
    try:
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = input("Введите путь к JSON-файлу: ").strip()
            transactions = load_transactions(file_path)
            if not transactions:
                print(f"Ошибка: Не удалось загрузить транзакции из {file_path}. Программа завершена.")
                return
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_path = input("Введите путь к CSV-файлу: ").strip()
            df = read_trans_from_csv(file_path)  # Мок должен перехватить вызов
            transactions = df.to_dict("records")  # Конвертация DataFrame в список словарей
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_path = input("Введите путь к XLSX-файлу: ").strip()
            df = read_trans_from_xls(file_path)
            transactions = df.to_dict("records")  # Конвертация DataFrame в список словарей
        else:
            print("Неверный выбор. Программа завершена.")
            return
    except Exception as e:
        print(f"Ошибка: {str(e)}. Программа завершена.")
        return

    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                "Пользователь: "
            )
            .strip()
            .upper()
        )
        if status in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status}"')
            transactions = filter_by_state(transactions, state=status)
            break
        print(f'Статус операции "{status}" недоступен.')

    # Сортировка по дате
    sort_by_date_option = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_by_date_option == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        descending = sort_order == "по убыванию"
        transactions = sort_by_date(transactions, descending=descending)

    # Фильтрация по рублям
    filter_rub = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if filter_rub == "да":
        transactions = [t for t in transactions if str(t.get("currency_code", "")) == "RUB"]

    # Фильтрация по слову в описании
    filter_desc = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if filter_desc == "да":
        search = input("Введите слово для поиска в описании: ").strip()
        transactions = process_bank_search(transactions, search)

    # Подсчёт операций по категориям
    categories = ["Перевод", "Открытие вклада", "Снятие наличных"]
    category_counts = process_bank_operations(transactions, categories)
    print("\nСтатистика по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count} операций")

    # Вывод результата
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        date = get_date(str(t.get("date", "")))
        amount = str(t.get("amount", ""))
        currency = str(t.get("currency_code", ""))
        description = str(t.get("description", ""))
        from_acc = mask_account_card(str(t.get("from", "")))
        to_acc = mask_account_card(str(t.get("to", "")))
        print(f"{date} {description}\n{from_acc} -> {to_acc}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
