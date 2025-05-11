from typing import Any

import pytest

import src.processing


@pytest.mark.parametrize("correct_operations_list_states", [i for i in range(4)], indirect=True)
def test_filter_by_state(correct_operations_list_states: Any) -> None:
    assert (
        src.processing.filter_by_state(*correct_operations_list_states["input"])
        == correct_operations_list_states["output"]
    )


@pytest.mark.parametrize("correct_operations_list_dates", [i for i in range(4)], indirect=True)
def test_sort_by_date(correct_operations_list_dates: Any) -> None:
    assert (
        src.processing.sort_by_date(*correct_operations_list_dates["input"]) == correct_operations_list_dates["output"]
    )


@pytest.mark.parametrize("incorrect_operations_list_dates", [i for i in range(2)], indirect=True)
def test_sort_by_incorrect_date(incorrect_operations_list_dates: Any) -> None:
    with pytest.raises(ValueError) as exc_info:
        src.processing.sort_by_date(*incorrect_operations_list_dates["input"])

    assert str(exc_info.value) == incorrect_operations_list_dates["output"]
