import pandas as pd
from typing import List, Dict


def read_financial_operations_from_csv(file_path: str) -> List[Dict]:
    """Считывает финансовые операции из CSV файла.

    Args:
        file_path (str): Путь к входному файлу CSV.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    # Используем параметр sep для указания разделителя
    df = pd.read_csv(file_path, sep=';')
    return df.to_dict(orient='records')


def read_financial_operations_from_excel(file_path: str) -> List[Dict]:
    """Считывает финансовые операции из Excel файла.

    Args:
        file_path (str): Путь к входному файлу Excel.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
