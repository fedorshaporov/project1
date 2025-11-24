import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция для поиска операций по описанию.

    :param data: Список словарей с транзакциями.
    :param search: Строка для поиска в описании.
    :return: Список словарей с транзакциями, содержащими строку поиска.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(transaction.get('description', ''))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция для подсчета количества операций по категориям.

    :param data: Список словарей с транзакциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством операций по категориям.
    """
    description_counter = Counter()

    # Подсчет операций по категориям
    for transaction in data:
        for category in categories:
            if category.lower() in transaction.get('description', '').lower():
                description_counter[category] += 1

    return dict(description_counter)
