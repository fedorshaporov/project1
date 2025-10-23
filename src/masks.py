def mask_card(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя первые 6 и последние 4 цифры открытыми,
    остальные заменяются звездочками.


    :param card_number: Номер кредитной карты.
    :return: Маскированный номер карты.
    """
    if len(card_number) >= 10:
        return f"{card_number[:6]} {'*' * (len(card_number) - 10)} {card_number[-4:]}"
    return f"{'*' * len(card_number)}"


def mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры открытыми.


    :param account_number: Номер счета.
    :return: Маскированный номер счета.
    """
    if len(account_number) > 4:
        return f"{'*' * (len(account_number) - 4)}{account_number[-4:]}"
    return account_number
