import json
import os
import requests
from dotenv import load_dotenv
from typing import List, Dict, Union

load_dotenv()


def read_json(filename: str) -> List[Dict]:
    """Читает JSON-файл и возвращает его содержимое в виде списка словарей.

    Args:
        filename (str): Путь к файлу JSON.

    Returns:
        List[Dict]: Список словарей из JSON-файла или пустой список при ошибке.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def convert_data(amount: Union[float, int], from_currency: str, to_currency: str) -> float:
    """Конвертирует указанную сумму из одной валюты в другую.

    Args:
        amount (float | int): Сумма для конвертации.
        from_currency (str): Исходная валюта.
        to_currency (str): Валюта для конвертации.

    Returns:
        float: Конвертированная сумма в целевой валюте.
    """
    url = (f"https://api.apilayer.com/exchangerates_data/"
           f"convert?to={to_currency}&from={from_currency}&amount={amount}")

    headers = {"apikey": os.getenv("EXCHANGE_RATES_API_KEY", "")}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return float(result.get("result", 0))
    else:
        raise ValueError(f"Error: {response.status_code} - {response.text}")
