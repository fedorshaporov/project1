def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param account_info: Строка с типом и номером карты/счета.
    :return: Строка с замаскированным номером.
    """
    account_type, account_number = account_info.split(maxsplit=1)

    if "Счет" in account_type:
        return f"{account_type} {mask_account(account_number)}"
    else:
        return f"{account_type} {mask_card(account_number)}"