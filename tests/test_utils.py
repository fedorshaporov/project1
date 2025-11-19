from unittest.mock import patch,mock_open
from src.utils import  read_json, convert_data

@patch("json.load")
def test_read_json(mock_load):
    with patch("builtins.open", mock_open()) as mocked_open:
        mock_load.return_value = {"test_1": "test_data"}
        result = read_json("dummy_data")
        expected = {"test_1": "test_data"}
        assert result == expected
