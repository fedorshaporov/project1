import json
import csv
import pandas as pd

from src.operations import process_bank_search


def load_transactions(filename: str, file_format: str) -> list[dict]:
    """
    Загружает транзакции из указанного файла в зависимости от формата.

    :param filename: Имя файла для загрузки.
    :param file_format: Формат файла ('json', 'csv', 'xlsx').
    :return: Список транзакций.
    """
    if file_format == 'json':
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif file_format == 'csv':
        with open(filename, mode='r', encoding='utf-8') as f:
            return [row for row in csv.DictReader(f)]
    elif file_format == 'xlsx':
        return pd.read_excel(filename).to_dict(orient='records')
    else:
        raise ValueError("Некорректный формат файла")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_choice = input("Выберите формат файла для загрузки (1. JSON, 2. CSV, 3. XLSX): ")

    formats = {'1': 'json', '2': 'csv', '3': 'xlsx'}
    if file_choice not in formats:
        print("Некорректный выбор формата.")
        return

    filename = input("Введите имя файла: ")
    transactions = load_transactions(filename, formats[file_choice])

    status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().lower()
    valid_statuses = {'executed', 'canceled', 'pending'}

    if status not in valid_statuses:
        print(f"Статус операции \"{status}\" недоступен.")
        return

    filtered_transactions = [t for t in transactions if t['status'].lower() == status]
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\".")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        ascending_order = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        if ascending_order == 'по возрастанию':
            filtered_transactions.sort(key=lambda x: x['date'])  # предположим, что есть поле 'date'
        elif ascending_order == 'по убыванию':
            filtered_transactions.sort(key=lambda x: x['date'], reverse=True)

    # Фильтрация по валюте
    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_filter == 'да':
        filtered_transactions = [t for t in filtered_transactions if t['currency'] == 'RUB']

    # Поиск по описанию
    description_search = input("Фильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if description_search == 'да':
        search_string = input("Введите строку для поиска: ")
        filtered_transactions = process_bank_search(filtered_transactions, search_string)

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Счет **{transaction['account']}\nСумма: {transaction['amount']} {transaction['currency']}\n")


if __name__ == "__main__":
    main()
