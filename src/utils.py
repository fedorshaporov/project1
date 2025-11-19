import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def read_json(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def convert_data(amount: float | int, from_currency: str, to_currency: str) -> float:
    url = (f"https://api.apilayer.com/exchangerates_data/"
           f"convert?to={to_currency}&from={from_currency}&amount={amount}")

    payload = {}
    headers = {"apikey": os.getenv("EXCHANGE_RATES_API_KEY", "")}
    response = requests.get(url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        return float(result["result"])
    else:
        return f"Error: {result}"

