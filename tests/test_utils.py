import pytest
from unittest.mock import patch, Mock, mock_open
from src.utils import  read_json, convert_data

# Тесты для функции read_json
def test_read_json_valid_file():
    test_json = '[{"amount": 100, "currency": "USD"}]'
    with patch("builtins.open", mock_open(read_data=test_json)):
        result = read_json("fake_path.json")
        assert result == [{"amount": 100, "currency": "USD"}]

def test_read_json_invalid_json():
    with patch("builtins.open", mock_open(read_data='not a json')):
        result = read_json("fake_path.json")
        assert result == []

def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json("fake_path.json")
        assert result == []

# Тесты для функции convert_data
@patch('requests.get')
def test_convert_data_success(mock_get):
    # Mocking the response of requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 7500}  # Пример результата
    mock_get.return_value = mock_response

    result = convert_data(100, 'USD', 'RUB')  # Пример вызова функции
    assert result == 7500.0

@patch('requests.get')
def test_convert_data_api_failure(mock_get):
    # Mocking the response of requests.get with an error status
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Error: 400 - Bad Request"):
        convert_data(100, 'USD', 'RUB')