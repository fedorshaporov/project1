import json
import os
import requests
import logging
from dotenv import load_dotenv
from typing import List, Dict, Union

load_dotenv()

# Настройка логирования
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'utils.log')

# Создаем директорию для логов, если она не существует
os.makedirs(LOG_DIR, exist_ok=True)

# Создаем логгер
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл, с перезаписью
file_handler = logging.FileHandler(LOG_FILE, mode='w')  # mode='w' для перезаписи
file_handler.setLevel(logging.DEBUG)

# Формат записи логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def read_json(filename: str) -> List[Dict]:
    """Читает JSON-файл и возвращает его содержимое в виде списка словарей.

    Args:
        filename (str): Путь к файлу JSON.

    Returns:
        List[Dict]: Список словарей из JSON-файла или пустой список при ошибке.
    """
    logger.info(f'Attempting to read JSON file: {filename}')
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Successfully read JSON file.")
                return data
            else:
                logger.warning("Data in JSON is not a list.")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f'Error reading JSON file: {e}')
        return []


def convert_data(amount: Union[float, int], from_currency: str, to_currency: str) -> float:
    """Конвертирует указанную сумму из одной валюты в другую.

    Args:
        amount (float | int): Сумма для конвертации.
        from_currency (str): Исходная валюта.
        to_currency (str): Валюта для конвертации.

    Returns:
        float: Конвертированная сумма в целевой валюте.

    Raises:
        ValueError: Если API возвращает ошибку.
    """
    logger.info(f'Converting {amount} {from_currency} to {to_currency}.')
    url = (f"https://api.apilayer.com/exchangerates_data/"
           f"convert?to={to_currency}&from={from_currency}&amount={amount}")

    headers = {"apikey": os.getenv("EXCHANGE_RATES_API_KEY", "")}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        logger.info(f'Successfully converted amount: {result.get("result", 0)}')
        return float(result.get("result", 0))
    else:
        logger.error(f'Error during conversion: {response.status_code} - {response.text}')
        raise ValueError(f"Error: {response.status_code} - {response.text}")


def main():
    # Пример использования функции read_json
    json_data = read_json('../data/operations.json')  # Убедитесь, что файл существует
    print("JSON Data:", json_data)

    # Пример использования функции convert_data
    try:
        converted_amount = convert_data(100, 'USD', 'RUB')  # Пример конвертации валюты
        print(f'Converted amount: {converted_amount}')
    except ValueError as e:
        print(f'Conversion failed: {e}')


if __name__ == "__main__":
    main()
