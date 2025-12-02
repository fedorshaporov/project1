import json
import csv
import pandas as pd
import re
from typing import List, Dict

# Определите пути к вашему справочнику файлов
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


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Запрашиваем пользователя о выбранном типе файла
    file_type_choice = input("Выберите тип файла для загрузки:\n1. JSON\n2. CSV\n3. XLSX\nВведите номер: ")

    if file_type_choice == '1':
        transactions = load_data(JSON_FILE, 'json')
    elif file_type_choice == '2':
        transactions = load_data(CSV_FILE, 'csv')
    elif file_type_choice == '3':
        transactions = load_data(XLSX_FILE, 'xlsx')
    else:
        print("Неверный выбор. Приложение будет завершено.")
        return

    # Выводим загруженные транзакции для отладки (можно убрать в финальной версии)
    print("Загруженные транзакции:")
    print(json.dumps(transactions, indent=4, ensure_ascii=False))

    # Шаг 1: Запрашиваем статус для фильтрации
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    selected_status = ''

    while selected_status not in valid_statuses:
        selected_status = input(f"Введите статус для фильтрации ({', '.join(valid_statuses)}): ").upper()
        if selected_status not in valid_statuses:
            print(f"Статус операции '{selected_status}' недоступен. Пожалуйста, попробуйте еще раз.")

    # Шаг 2: Фильтрация по статусу
    filtered_transactions = [t for t in transactions if t.get('state', '').upper() == selected_status]
    print(f"Количество транзакций после фильтрации: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Шаг 3: Сортировка по дате
    if input("Отсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Сортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").lower()
        filtered_transactions.sort(key=lambda x: x.get('date'), reverse=(order == 'убыванию'))

    # Шаг 4: Фильтрация только рублевых транзакций
    if input("Выводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        filtered_transactions = [
            t for t in filtered_transactions
            if 'operationAmount' in t and
               t['operationAmount'].get('currency', {}).get('code', '').upper() == 'RUB'
        ]

    # Шаг 5: Поиск по слову в описании
    if input("Отфильтровать по слову в описании? (да/нет): ").lower() == 'да':
        search_term = input("Введите строку для поиска в описании: ")
        filtered_transactions = process_bank_search(filtered_transactions, search_term)

    # Шаг 6: Вывод результатов
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Вывод в нужном формате
    for transaction in filtered_transactions:
        date_info = transaction.get('date', 'Нет даты')
        description_info = transaction.get('description', 'Нет описания')
        account_info = transaction.get('account', 'Нет информации о счете')
        amount_info = transaction.get('operationAmount', {}).get('amount', 'Нет суммы')
        currency_info = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'Нет валюты')

        # Формат вывода
        print(f"{date_info.split('T')[0]} - {description_info}\nСчет: **{account_info}\nСумма: {amount_info} {currency_info}\n")

if __name__ == "__main__":
    main()
