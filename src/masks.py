import logging
import os

# Настройка логирования
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'masks.log')

# Создаем директорию для логов, если она не существует
os.makedirs(LOG_DIR, exist_ok=True)

# Создаем логгер
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи логов в файл, с перезаписью
file_handler = logging.FileHandler(LOG_FILE, mode='w')  # mode='w' для перезаписи
file_handler.setLevel(logging.DEBUG)

# Формат записи логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

def mask_card(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя первые 6 и последние 4 цифры открытыми,
    остальные заменяются звездочками.

    :param card_number: Номер кредитной карты.
    :return: Маскированный номер карты.
    """
    logger.info(f'Masking card number: {card_number}')

    if len(card_number) >= 10:
        masked = f"{card_number[:6]} ** ** {card_number[-4:]}"
        logger.info(f'Masked card number: {masked}')
        return masked

    logger.warning("Card number is too short, masking entire number.")
    return '*' * len(card_number)

def mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры открытыми.

    :param account_number: Номер счета.
    :return: Маскированный номер счета.
    """
    logger.info(f'Masking account number: {account_number}')

    if len(account_number) > 4:
        masked = '**' + account_number[-4:]
        logger.info(f'Masked account number: {masked}')
        return masked

    logger.warning("Account number is too short, returning the original number.")
    return account_number

def main():
    # Пример маскировки номера карты
    print(mask_card("1234567890123456"))  # Ожидается маска
    print(mask_card("123"))                # Ожидается предупреждение

    # Пример маскировки номера счета
    print(mask_account("123456789012"))    # Ожидается маска
    print(mask_account("123"))              # Ожидается оригинал

if __name__ == "__main__":
    main()