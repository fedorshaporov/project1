import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Возвращает список транзакций, описания которых содержат строку поиска."""
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр
    return [transaction for transaction in data if pattern.search(transaction.get('description', ''))]

def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Возвращает словарь, где ключи - названия категорий, а значения - количество операций."""
    operation_count = {category: 0 for category in categories}

    for transaction in data:
        for category in categories:
            if category.lower() in transaction.get('description', '').lower():
                operation_count[category] += 1

    return operation_count
