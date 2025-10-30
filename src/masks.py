def mask_card(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя первые 6 и последние 4 цифры открытыми,
    остальные заменяются звездочками.

    :param card_number: Номер кредитной карты.
    :return: Маскированный номер карты.
    """
    if len(card_number) >= 10:
        return f"{card_number[:6]}{'*' * (len(card_number) - 10)}{card_number[-4:]}"
    return '*' * len(card_number)

def mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры открытыми.

    :param account_number: Номер счета.
    :return: Маскированный номер счета.
    """
    if len(account_number) > 4:
        return '*' * (len(account_number) - 4) + account_number[-4:]
    return account_number

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    :param info: Строка, содержащая тип (карта или счет) и номер.
    :return: Строка с замаскированным номером.
    """
    card_types = ['Visa', 'MasterCard', 'Maestro']

    for card_type in card_types:
        if info.startswith(card_type):
            card_number = info.split(" ")[-1]
            masked_number = mask_card(card_number)
            return info.replace(card_number, masked_number)

    if info.startswith('Счет'):
        account_number = info.split(" ")[-1]
        masked_account = mask_account(account_number)
        return info.replace(account_number, masked_account)

    return info  # Если ничего не найдено, возвращаем исходную строку
