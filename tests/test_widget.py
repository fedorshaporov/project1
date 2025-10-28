import unittest

from widget import get_date, mask_account_card


class TestWidget(unittest.TestCase):

    def test_mask_account_card(self):
        self.assertEqual(mask_account_card("Visa Platinum 7000792289606361"),
                         "Visa Platinum 700079 ****** 6361")
        self.assertEqual(mask_account_card("Счет 73654108430135874305"),
                         "Счет ****************4305")

    def test_get_date(self):
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")


if __name__ == "__main__":
    unittest.main()


import pytest
from src.masks import mask_account, mask_card  # Импортируйте функции маскировки
from src.widget import mask_account_card  # Замените 'widget' на реальное имя вашего модуля

@pytest.fixture
def mock_masks(monkeypatch):
    # Mock функции маскировки для тестов
    def mock_mask_account(account_number):
        return "****1234"  # Пример замаскированного номера счета

    def mock_mask_card(card_number):
        return "**** **** **** 3456"  # Пример замаскированного номера карты

    monkeypatch.setattr('src.masks.mask_account', mock_mask_account)
    monkeypatch.setattr('src.masks.mask_card', mock_mask_card)

def test_mask_account_card_card(mock_masks):
    input_info = "Visa 1234567890123456"
    expected_output = "Visa **** **** **** 3456"
    assert mask_account_card(input_info) == expected_output

def test_mask_account_card_account(mock_masks):
    input_info = "Счет 123456789012"
    expected_output = "Счет ****1234"
    assert mask_account_card(input_info) == expected_output

def test_mask_account_card_invalid_type(mock_masks):
    input_info = "UnknownType 1234567890"
    expected_output = "UnknownType 1234567890"  # Не должно быть замены
    assert mask_account_card(input_info) == expected_output

    from src.widget import get_date
    from datetime import datetime

    def test_get_date_valid():
        input_date = "2019-07-03T18:35:29.512364"
        expected_output = "03.07.2019"
        assert get_date(input_date) == expected_output

    def test_get_date_invalid():
        input_date = "invalid-date-string"
        with pytest.raises(ValueError):
            get_date(input_date)


