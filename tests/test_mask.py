import pytest
from src.masks import mask_card

def test_mask_card():
    # Проверка с нормально работающим номером карты
    assert mask_card("1234567890123456") == "123456****3456"

    # Проверка с номером карты менее 10 символов
    assert mask_card("1234") == "****"

    # Проверка с номером карты больше 10 символов, но с пустотой
    assert mask_card("123456") == "123456"

    # Проверка с номером карты, состоящим только из звездочек
    assert mask_card("") == ""

    from src.masks import mask_account

    def test_mask_account():
        # Проверка с нормально работающим номером счета
        assert mask_account("123456789012") == "*********012"

        # Проверка с номером счета менее 4 символов
        assert mask_account("123") == "123"

        # Проверка с номером счета ровно 4 символа
        assert mask_account("1234") == "1234"

        # Проверка с номером счета, состоящим только из звездочек
        assert mask_account("") == ""


        @pytest.mark.parametrize("input_card, expected_output", [
            ("1234567890123456", "123456****3456"),
            ("1234", "****"),
            ("123456", "123456"),
            ("", ""),
        ])
        def test_mask_card_parametrized(input_card, expected_output):
            assert mask_card(input_card) == expected_output

        @pytest.mark.parametrize("input_account, expected_output", [
            ("123456789012", "*********012"),
            ("123", "123"),
            ("1234", "1234"),
            ("", ""),
        ])
        def test_mask_account_parametrized(input_account, expected_output):
            assert mask_account(input_account) == expected_output
