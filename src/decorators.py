from typing import Any, Callable


def loggerr(filename: str | None = None) -> Callable:
    """
       Декоратор для логирования выполнения функций.

       :filename: Имя файла, в который будут сохраняться логи.
                        Если None, логи будут выводиться в консоль.
       :return: Декорированная функция.
       """

    def deco(func: Callable) -> Callable:
        """
               Внутренний декоратор, который оборачивает функцию.

               :func: Декорируемая функция.
               :return: Обернутая функция с логированием.
               """
        def write_log(msg: str):
            """
                       Записывает сообщение в файл или выводит в консоль.
                       :param msg: Сообщение для записи.
                       """
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(msg + "\n")
            else:
                print(msg)

        def wrapper(*args, **kwargs) -> Any:
            """
            Обертка для обработки логики выполнения функции.

            :param args: Позиционные аргументы для передаваемой функции.
            :param kwargs: Именованные аргументы для передаваемой функции.
            :return: Результат выполнения функции.
            :raises: Ошибка, если выполнение функции завершается исключением.
            """
            try:
                result = func(*args, **kwargs)
                msg = f"Функция {func.__name__} выполнена!"
                write_log(msg)
                return result
            except Exception as e:
                msg = (f"Функция {func.__name__} не выполнена! Произошла ошибка {type(e).__name__}: {e},"
                       f"входные параметры: {args, kwargs}.")
                write_log(msg)
                raise
        return wrapper
    return deco
