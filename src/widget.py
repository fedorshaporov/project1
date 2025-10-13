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

    def get_date(date_str: str) -> str:
        """Конвертирует дату из ISO-формата в формат ДД.ММ.ГГГГ.

        :param date_str: Дата в формате "2024-03-11T02:26:18.671407".
        :return: Дата в формате "ДД.ММ.ГГГГ".
        """
        date_object = datetime.fromisoformat(date_str)
        return date_object.strftime("%d.%m.%Y")
