import os
from pathlib import Path
from typing import Any

import pytest

import src.decorators


@pytest.mark.parametrize("log_decoration", [i for i in range(2)], indirect=True)
def test_log_to_file(log_decoration: dict) -> None:
    @src.decorators.log(filename=os.path.join(Path(__file__).resolve().parents[1], "tests", "test_logs", "logs.txt"))
    def sum_a_b(*args: int) -> int:
        return sum(args)

    with open(os.path.join(Path(__file__).resolve().parents[1], "tests", "test_logs", "logs.txt"), "w") as file:
        file.write("")

    sum_a_b(*log_decoration["input"])

    with open(os.path.join(Path(__file__).resolve().parents[1], "tests", "test_logs", "logs.txt"), "r") as file:
        logstring = file.read()

    log_string_to_check_1 = logstring[28: logstring.index("at") + 3]
    log_string_to_check_2 = logstring[logstring.index("at") + 32:]

    assert log_string_to_check_1 + log_string_to_check_2 == log_decoration["output"]


@pytest.mark.parametrize("log_decoration", [i for i in range(2)], indirect=True)
def test_log_to_console(log_decoration: dict, capsys: Any) -> None:
    @src.decorators.log()
    def sum_a_b(*args: int) -> int:
        return sum(args)

    sum_a_b(*log_decoration["input"])

    logstring = capsys.readouterr().out

    log_string_to_check_1 = logstring[28: logstring.index("at") + 3]
    log_string_to_check_2 = logstring[logstring.index("at") + 32:]

    assert log_string_to_check_1 + log_string_to_check_2 == log_decoration["output"]
