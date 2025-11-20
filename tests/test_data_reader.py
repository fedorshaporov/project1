import pytest
from unittest.mock import patch, MagicMock
from src.data_reader import read_financial_operations_from_csv, read_financial_operations_from_excel


# Тесты для функции считывания из CSV
@patch('pandas.read_csv')
def test_read_financial_operations_from_csv(mock_read_csv):
    # Настройка мока
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{'amount': 100, 'currency': 'USD'}, {'amount': 200, 'currency': 'EUR'}]
    mock_read_csv.return_value = mock_data

    result = read_financial_operations_from_csv('fake_path.csv')

    # Проверка результата
    assert result == [{'amount': 100, 'currency': 'USD'}, {'amount': 200, 'currency': 'EUR'}]
    mock_read_csv.assert_called_once_with('fake_path.csv', sep=';')


# Тесты для функции считывания из Excel
@patch('pandas.read_excel')
def test_read_financial_operations_from_excel(mock_read_excel):
    # Настройка мока
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{'amount': 150, 'currency': 'USD'}, {'amount': 300, 'currency': 'JPY'}]
    mock_read_excel.return_value = mock_data

    result = read_financial_operations_from_excel('fake_path.xlsx')

    # Проверка результата
    assert result == [{'amount': 150, 'currency': 'USD'}, {'amount': 300, 'currency': 'JPY'}]
    mock_read_excel.assert_called_once_with('fake_path.xlsx')
