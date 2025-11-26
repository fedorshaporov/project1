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
## Модуль generators
  ## Описание:
  Модуль generators содержит функции-генераторы для обработки и анализа данных транзакций.
  ## функции
  # filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]
  Фильтрует транзакции по заданной валюте и возвращает генератор подходящих транзакций.
  # Пример использования:
  usd_transactions = filter_by_currency(transactions, "USD")
  for transaction in usd_transactions:
  print(transaction)
  # transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]  
  Возвращает описание каждой транзакции по очереди.
  # Пример использования:
  descriptions = transaction_descriptions(transactions)
  for description in descriptions:
  print(description)
  # card_number_generator(start: int, end: int) -> Iterator[str]
  Генерирует номера банковских карт в заданном диапазоне.
  # Пример использования:
  for card_number in card_number_generator(1, 5):
  print(card_number)
## Новая функциональность
  # Библиотеки csv и pandas
  # Чтение финансовых операций из CSV-файлов
  Реализована функция read_financial_operations_from_csv, которая считывает финансовые данные из файла CSV.
  Функция принимает путь к файлу CSV в качестве аргумента и возвращает список словарей с транзакциями.
  # Чтение финансовых операций из Excel-файлов
  Реализована функция read_financial_operations_from_excel, которая считывает финансовые данные из файла Excel (XLSX).
  Функция принимает путь к файлу Excel в качестве аргумента и возвращает список словарей с транзакциями.
  ## Банковские Транзакции
  Программа для обработки и анализа банковских транзакций. Пользователи могут загружать транзакции из различных форматов файлов, фильтровать данные по статусу, сортировать их по дате, а также выполнять поиск   операций по описанию.
  ## Описание
  Данный проект позволяет пользователям:
  * Загружать данные из файлов форматов JSON, CSV и XLSX.
  * Фильтровать транзакции по статусам (EXECUTED, CANCELED, PENDING).
  * Сортировать транзакции по дате.
  * Выполнять поиск по описанию транзакций с использованием регулярных выражений.
  ## Функции программы

- **load_transactions**: Загружает транзакции из файла.
- **process_bank_search**: Выполняет поиск транзакций по заданному описанию.
- **process_bank_operations**: Подсчитывает количество транзакций по категориям.

  
## Лицензия:
     Этот проект лицензирован под [MIT License](LICENSE).
## Контакты:
     Если у вас есть вопросы, свяжитесь со мной по email: shaporovfed@gmail.com
 
   
