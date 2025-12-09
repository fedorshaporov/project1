from src.masks import mask_account, mask_card


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param info: Строка формата 'Тип 1234567890123456'
    :return: Строка с замаскированным номером или пустая строка для недопустимых входных данных
    """
    # Проверка типа данных и пустой строки
    if not isinstance(info, str) or not info.strip():
        return ""  # Возвращаем безопасное значение, если это не строка или строка пустая

    type_, number = info.split(maxsplit=1)

    if 'Счет' in type_:
        return f"{type_} {mask_account(number)}"
    else:  # Ожидаем, что это карта
        return f"{type_} {mask_card(number)}"

def get_date(date_str: str) -> str:
    """
    Преобразует строку даты в формат 'ДД.ММ.ГГГГ'.

    :param date_str: Дата в формате 'YYYY-MM-DDTHH:MM:SS'
    :return: Дата в формате 'ДД.ММ.ГГГГ'
    """
    from datetime import datetime
    date = datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")
