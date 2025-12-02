import json
import csv
import pandas as pd
import re
from typing import List, Dict

# Определите пути к вашим файлам
JSON_FILE = '../data/operations.json'  # Путь к файлу JSON
CSV_FILE = '../data/transactions.csv'   # Путь к файлу CSV
XLSX_FILE = '../data/transactions_excel.xlsx'  # Путь к файлу XLSX


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Поиск транзакций по описанию с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(transaction.get('description', ''))]


def load_data(file_path: str, file_type: str) -> List[Dict]:
    """Загрузка данных из файлов: JSON, CSV, XLSX."""
    if file_type == 'json':
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif file_type == 'csv':
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif file_type == 'xlsx':
        return pd.read_excel(file_path).to_dict(orient='records')
    else:
        raise ValueError("Unsupported file type.")


def filter_transactions_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация транзакций по статусу."""
    return [t for t in transactions if t.get('state', '').upper() == status]


def sort_transactions(transactions: List[Dict], order: str) -> List[Dict]:
    """Сортировка транзакций по дате."""
    return sorted(transactions, key=lambda x: x['date'], reverse=(order == 'убыванию'))


def filter_ruble_transactions(transactions: List[Dict]) -> List[Dict]:
    """Фильтрует только рублевые транзакции."""
    return [
        t for t in transactions
        if 'operationAmount' in t and
           t['operationAmount']['currency']['code'].upper() == 'RUB'
    ]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Шаг 1: Выбор типа файла
    file_type_choice = input("Выберите тип файла для загрузки:\n1. JSON\n2. CSV\n3. XLSX\nПользователь: ")

    if file_type_choice == '1':
        transactions = load_data(JSON_FILE, 'json')
    elif file_type_choice == '2':
        transactions = load_data(CSV_FILE, 'csv')
    elif file_type_choice == '3':
        transactions = load_data(XLSX_FILE, 'xlsx')
    else:
        print("Неверный выбор. Пожалуйста, введите '1', '2' или '3'.")
        return

    # Шаг 2: Запрашиваем статус для фильтрации
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    selected_status = ''

    while selected_status not in valid_statuses:
        selected_status = input(f"Введите статус для фильтрации ({', '.join(valid_statuses)}): ").upper()
        if selected_status not in valid_statuses:
            print(f"Статус операции '{selected_status}' недоступен. Пожалуйста, попробуйте еще раз.")

    # Фильтруем транзакции по статусу
    filtered_transactions = filter_transactions_by_status(transactions, selected_status)
    print(f"Количество транзакций после фильтрации: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Шаг 3: Сортировка
    if input("Отсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Сортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").lower()
        filtered_transactions = sort_transactions(filtered_transactions, order)

    # Шаг 4: Фильтрация только рублевых транзакций
    if input("Выводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        filtered_transactions = filter_ruble_transactions(filtered_transactions)

    # Шаг 5: Поиск по слову в описании
    if input("Отфильтровать по слову в описании? (да/нет): ").lower() == 'да':
        search_term = input("Введите строку для поиска в описании: ")
        filtered_transactions = process_bank_search(filtered_transactions, search_term)

    # Вывод результатов
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    for transaction in filtered_transactions:
        date_info = transaction.get('date', 'Нет даты')
        description_info = transaction.get('description', 'Нет описания')
        account_info = transaction.get('account', 'Нет информации о счете')
        amount_info = transaction.get('operationAmount', {}).get('amount', 'Нет суммы')
        currency_info = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'Нет валюты')

        print(f"{date_info} - {description_info}\nСчет: **{account_info}\nСумма: {amount_info} {currency_info}\n")

if __name__ == "__main__":
    main()
