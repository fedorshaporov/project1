import functools
import logging

def log(filename: str = None):
    """Декоратор для логирования работы функции."""
    # Настройка логирования
    logger = logging.getLogger(__name__)
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Starting '{func.__name__}' with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"'{func.__name__}' ok, result: {result}")
                return result
            except Exception as e:
                logger.error(f"'{func.__name__}' error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

# Пример вызова функции
my_function(1, 2)