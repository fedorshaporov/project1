def mask_account_card(card_info: str) -> str:
    """Маскирует номер карты или счета.

    :param card_info: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    card_type, card_number = card_info.split(maxsplit=1)
    if 'Счет' in card_type:
        return mask_account(card_number)
    else:
        return mask_card(card_number)
