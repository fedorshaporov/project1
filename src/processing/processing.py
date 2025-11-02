from typing import List, Dict, Union


def filter_by_state(data: List[Dict[str, Union[int, str]]], state: str = 'EXECUTED') -> List[Dict[str, Union[int, str]]]:
    """Фильтрует список словарей по значению ключа state."""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, Union[int, str]]], reverse: bool = True) -> List[Dict[str, Union[int, str]]]:
    """Сортирует список словарей по дате."""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)


# Пример данных с четко определенными типами
example_data: List[Dict[str, Union[int, str]]] = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]


# Вызов функции с состоянием по умолчанию
executed_items = filter_by_state(example_data)
print("Executed items:", executed_items)


# Вызов функции с состоянием 'CANCELED'
canceled_items = filter_by_state(example_data, 'CANCELED')
print("Canceled items:", canceled_items)


# Пример использования функции сортировки
sorted_data = sort_by_date(example_data)
print("Sorted data:", sorted_data)
