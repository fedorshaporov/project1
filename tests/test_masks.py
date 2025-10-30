from project1.src.masks import mask_card, mask_account

def test_mask_card():
    """Тестирование маскирования номера карты."""
    assert mask_card("7000792289606361") == "7000 **** **** 6361"
    assert mask_card("1234567812345678") == "123456 **** **** 5678"
    assert mask_card("12345") == "*****"

def test_mask_account():
    """Тестирование маскирования номера счета."""
    assert mask_account("73654108430135874305") == "**********4305"
    assert mask_account("1234") == "1234"
    assert mask_account("") == ""  # Тест на пустую строку