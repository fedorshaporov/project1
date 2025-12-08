import re
from typing import List, Dict
from src.utils import read_json
from src.data_reader import read_financial_operations_from_csv, read_financial_operations_from_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.widget import mask_account_card, get_date


# Определите пути к вашим файлам
JSON_FILE = '../data/operations.json'  # Путь к файлу JSON
CSV_FILE = '../data/transactions.csv'   # Путь к файлу CSV
XLSX_FILE = '../data/transactions_excel.xlsx'  # Путь к файлу XLSX


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Поиск транзакций по описанию с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(transaction.get('description', ''))]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Шаг 1: Выбор типа файла
    file_type_choice = input("Выберите тип файла для загрузки:\n1. JSON\n2. CSV\n3. XLSX\nПользователь: ")

    if file_type_choice == '1':
        transactions = read_json(JSON_FILE)
    elif file_type_choice == '2':
        transactions = read_financial_operations_from_csv(CSV_FILE)
    elif file_type_choice == '3':
        transactions = read_financial_operations_from_excel(XLSX_FILE)
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
    filtered_transactions = filter_by_state(transactions, selected_status)
    print(f"Количество транзакций после фильтрации: {len(filtered_transactions)}")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Шаг 3: Сортировка
    if input("Отсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Сортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").lower()
        if order == "возрастанию":
            order_bool = False
        else:
            order_bool = True
        filtered_transactions = sort_by_date(filtered_transactions, order_bool)

    # Шаг 4: Фильтрация только рублевых транзакций
    if input("Выводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        filtered_transactions =list(filter_by_currency(filtered_transactions,"RUB"))

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
        date_info = get_date(transaction.get('date', 'Нет даты'))
        description_info = transaction.get('description', 'Нет описания')
        if transaction.get("to"):
            account_info = f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}"
        else:
            account_info = f"{mask_account_card(transaction["from"])}"
        if transaction.get('operationAmount'):
            amount_info = transaction.get('operationAmount', {}).get('amount', 'Нет суммы')
            currency_info = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'Нет валюты')
        else:
            amount_info = transaction.get('amount', {})
            currency_info = transaction.get('currency_code', {})

        print(f"{date_info} - {description_info}\n{account_info}\nСумма: {amount_info} {currency_info}\n")


if __name__ == "__main__":
    main()
