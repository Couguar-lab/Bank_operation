import csv
from pathlib import Path

import pandas as pd


# Функция чтения данных о транзакциях из файла csv
def read_trans_from_csv(file_path: str):
    """Функция принимает в качестве аргумента путь к файлу csv и возвращает список словарей с транзакциями"""
    file_path = Path(file_path)  # Преобразовываем путь
    with open(file_path, encoding="utf-8") as file:  # Читаем и декодируем файл по указанному пути
        data_csv = csv.DictReader(file, delimiter=";")
        df_csv = pd.DataFrame(data_csv)
        transactions_csv = df_csv.to_dict(orient="records")
    return transactions_csv  # Возвращаем список словарей


# print(read_trans_from_csv('../data/transactions.csv'))


# Функция чтения данных о транзакциях из файла excel
def read_trans_from_xls(file_path: str):
    """Функция принимает в качестве аргумента путь к файлу csv и возвращает список словарей с транзакциями"""
    file_path = Path(file_path)  # Преобразовываем путь
    df = pd.read_excel(file_path)
    transactions_xls = df.to_dict(orient="records")
    return transactions_xls  # Возвращаем список словарей


# print(read_trans_from_xls('../data/transactions_excel.xlsx'))
