from src.masks import mask_account, mask_card  # Импортируйте функции маскировки


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.


    :param info: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    card_types = ['Visa', 'MasterCard', 'Maestro']

    # Извлечение номера карты/счета из строки
    for card_type in card_types:
        if info.startswith(card_type):
            # Маскируем номер карты
            card_number = info.split(' ')[-1]  # Получаем только номер
            masked_number = mask_card(card_number)
            return info.replace(card_number, masked_number)  # Возвращаем с замаскированным номером

    # Маскируем номер счета
    if info.startswith('Счет'):
        account_number = info.split(' ')[-1]  # Получаем только номер
        masked_account = mask_account(account_number)
        return info.replace(account_number, masked_account)  # Возвращаем с замаскированным номером

    return info  # Если ничего не найдено, возвращаем исходную строку


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты в формат ДД.ММ.ГГГГ.


    :param date_string: Дата в формате ISO.
    :return: Дата в формате ДД.ММ.ГГГГ.
    """
    from datetime import datetime
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")
