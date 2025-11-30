import json
import csv
import pandas as pd
from pathlib import Path
from typing import List, Dict
import re
from src.operations import process_bank_search


def load_data(file_path: Path) -> List[Dict]:
    """Загружает данные из выбранного файла."""
    data = []

    if file_path.suffix == '.json':
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")

    elif file_path.suffix == '.csv':
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла CSV: {e}")

    elif file_path.suffix == '.xlsx':
        try:
            data = pd.read_excel(file_path).to_dict(orient='records')
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла XLSX: {e}")

    return data


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice not in ['1', '2', '3']:
        print("Некорректный выбор.")
        return

    # Запрашиваем статус
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    status = ''
    while status not in valid_statuses:
        status = input(f"Введите статус для фильтрации ({', '.join(valid_statuses)}): ").upper()
        if status not in valid_statuses:
            print(f"Статус операции '{status}' недоступен. Пожалуйста, попробуйте еще раз.")

    # Запрашиваем имя файла после статуса
    filename = input("Введите имя файла (с учетом расширения): ")
    file_path = Path("../data") / filename

    # Загружаем данные
    data = load_data(file_path)
    if not data:  # Проверяем на наличие загруженных данных
        return

    # Фильтруем данные по статусу
    filtered_data = [transaction for transaction in data if transaction.get('state', '').upper() == status]

    print(f"Операции отфильтрованы по статусу: {status}")

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Сортировка операций
    if input("Отсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Сортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").lower()
        filtered_data.sort(key=lambda x: x['date'], reverse=(order == 'убыванию'))

    # Фильтрация только рублевых транзакций
    if input("Выводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        filtered_data = [
            t for t in filtered_data
            if 'operationAmount' in t and
            'currency' in t['operationAmount'] and
            t['operationAmount']['currency']['code'].upper() == 'RUB'
        ]

    # Фильтрация по слову в описании
    if input("Отфильтровать по слову в описании? (да/нет): ").lower() == 'да':
        search_term = input("Введите слово для поиска в описании: ")
        filtered_data = process_bank_search(filtered_data, search_term)

    # Вывод результатов
    print(f"Всего банковских операций в выборке: {len(filtered_data)}")

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    for transaction in filtered_data:
        account_info = transaction.get('account', 'Нет информации о счете')
        date_info = transaction.get('date', 'Нет даты')
        description_info = transaction.get('description', 'Нет описания')
        amount_info = transaction.get('amount', 'Нет суммы')
        currency_info = transaction.get('currency', 'Нет валюты')

        print(
            f"{date_info} {description_info}\nСчет **{account_info}\nСумма: {amount_info} {currency_info}\n"
        )

if __name__ == "__main__":
    main()