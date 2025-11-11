import pathlib
import pytest
from src.decorators import loggerr

def test_success_logs_in_console(capsys):

    @loggerr()
    def foo(a, b):
        return a + b

    result = foo(2, 3)
    assert result == 5
    capture = capsys.readouterr()
    assert capture.out == f"Функция foo выполнена!\n"

def test_error_logs_in_file(tmp_path: pathlib.Path):
    log_file = tmp_path / "log.txt"

    @loggerr(str(log_file))
    def foo(a, b):
        return a + b

    with pytest.raises(TypeError):
         foo(1, "2")

    content = log_file.read_text(encoding="utf-8")
    # assert content =="Функция foo не выполнена! Произошла ошибка TypeError: unsupported operand type(s) for +: 'int' and 'str',входные параметры: ((1, '2'), {}).\n"
    assert "Функция foo не выполнена!" in content
    assert "Произошла ошибка TypeError" in content
    assert "входные параметры: ((1, '2'), {})" in content
