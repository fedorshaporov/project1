# Проект: Виджет банковских операций
## Описание
Этот проект предназначен для обработки и отображения банковских операций клиентов.
## Основные функции:
* Фильтрация транзакций
* Сортировка транзакций
## Установка
1. Клонируйте репозиторий:
```
git clone https://github.com/user/project1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
## Функции
1. filter_by_state(transactions: List[Dict[str, Union[int, str]]], state: str = 'EXECUTED') -> List[Dict[str, Union[int, str]]]
  * ## Описание:
    Функция принимает список словарей с данными о банковских операциях и возвращает новый список, содержащий только те записи, у которых ключ state соответствует переданному значению.
  * ## Параметры:
    * transactions: Список операций (тип: List[Dict[str, Union[int, str]]]).
    * state: Статус для фильтрации (по умолчанию EXECUTED).
* ## Пример использования:
  transactions = [
  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

executed_transactions = filter_by_state(transactions)
print(executed_transactions)
2. sort_by_date(transactions: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]
  * ## Описание:
    Функция принимает список операций и возвращает новый список, отсортированный по дате (по умолчанию сортировка идет по убыванию).
  * ## Параметры:
    * transactions: Список операций (тип: List[Dict[str, str]]).
    * reverse: Порядок сортировки (по умолчанию True – убывание).
  * ## Пример использования:
     python sorted_transactions = sort_by_date(transactions) print(sorted_transactions)
## Тестирование:
     Для запуска тестов используйте следующую команду: python -m unittest discover
## Лицензия:
     Этот проект лицензирован под [MIT License](LICENSE).
## Контакты:
     Если у вас есть вопросы, свяжитесь со мной по email: shaporovfed@gmail.com
 
   
