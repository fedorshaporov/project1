from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Генератор, который фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount"):
            if transaction['operationAmount']['currency']['code'] == currency:
                yield transaction
        else:
            if transaction['currency_code'] == currency:
                yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        formatted_number = f"{num:016d}"
        yield ' '.join(formatted_number[i:i + 4] for i in range(0, 16, 4))
