import json
import csv
import pandas as pd
import re
from typing import List, Dict


# Определите пути к вашим файлам
JSON_FILE = '../data/operations.json'  # Путь к файлу JSON
CSV_FILE = '../data/transactions.csv'    # Путь к файлу CSV
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


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Шаг 1: Загрузка данных
    transactions = load_data(JSON_FILE, 'json')
    print("Загруженные транзакции:")
    print(json.dumps(transactions, indent=4, ensure_ascii=False))  # Для отладки

    # Шаг 2: Запрос статуса для фильтрации
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    selected_status = ''

    while selected_status not in valid_statuses:
        selected_status = input(f"Введите статус для фильтрации ({', '.join(valid_statuses)}): ").upper()
        if selected_status not in valid_statuses:
            print(f"Статус операции '{selected_status}' недоступен. Пожалуйста, попробуйте еще раз.")

    # Шаг 3: Фильтрация по статусу
    filtered_transactions = [t for t in transactions if t.get('state', '').upper() == selected_status]
    print(f"Количество транзакций после фильтрации: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Шаг 4: Сортировка
    sort_choice = input("Отсортировать операции по дате? (да/нет): ").strip().lower()
    if sort_choice == 'да':
        order_choice = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").strip().lower()
        filtered_transactions.sort(key=lambda x: x.get('date'), reverse=(order_choice == 'убыванию'))

    # Шаг 5: Фильтрация рублевых транзакций
    currency_filter = input("Выводить только рублевые транзакции? (да/нет): ").strip().lower()
    if currency_filter == 'да':
        filtered_transactions = [
            t for t in filtered_transactions
            if 'operationAmount' in t and
               'currency' in t['operationAmount'] and
               t['operationAmount']['currency']['code'].upper() == 'RUB'
        ]

    # Шаг 6: Поиск по слову в описании
    search_word = input("Отфильтровать список транзакций по определенному слову в описании? (да/нет): ").strip().lower()
    if search_word == 'да':
        search_term = input("Введите строку для поиска: ")
        filtered_transactions = process_bank_search(filtered_transactions, search_term)

    # Шаг 7: Вывод результатов
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
