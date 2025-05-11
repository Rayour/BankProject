"""
Модуль с декораторами
"""

from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(*, filename: Optional[str] = None) -> Any:
    """
    Декоратор. Логирует информацию о работе функции в файл, переданный в именованном аргументе 'filename'
    или в консоль, если имя файла не указано.
    Логируется:
    * время запуска функции
    * время завершения работы функции
    * имя функции
    * переданные аргументы
    * результат выполнения при успешном выполнении
    * ошибка при возниконовении исключения
    """

    def wrapper(function: Callable) -> Any:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> None:
            time_start = datetime.now()
            function_name = function.__name__
            arguments = [args, kwargs]
            is_ok = True
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                error_value = e
                time_finish = datetime.now()
                is_ok = False
            else:
                function_result = str(result)
                time_finish = datetime.now()
            finally:
                if filename:
                    with open(filename, "a") as file:
                        if is_ok:
                            file.write(
                                f"""[{time_start}][INFO] Function {function_name}({arguments}) successfully finished \
at [{time_finish}] with result {function_result}\n"""
                            )
                        else:
                            file.write(
                                f"""[{time_start}][ERROR] Function {function_name}({arguments}) failed at \
[{time_finish}] with error "{error_value}"\n"""
                            )
                else:
                    if is_ok:
                        print(
                            f"""[{time_start}][INFO] Function {function_name}({arguments}) successfully finished \
at [{time_finish}] with result {function_result}"""
                        )
                    else:
                        print(
                            f'''[{time_start}][ERROR] Function {function_name}({arguments}) failed at \
[{time_finish}] with error "{error_value}"'''
                        )

        return inner

    return wrapper
