import pytest

import src.processing


@pytest.mark.parametrize("correct_operations_list_states", [(0), (1), (2), (3)], indirect=True)
def test_filter_by_state(correct_operations_list_states):
    assert src.processing.filter_by_state(*correct_operations_list_states["input"]) == correct_operations_list_states[
        "output"]


@pytest.mark.parametrize("correct_operations_list_dates", [(0), (1), (2), (3)], indirect=True)
def test_sort_by_date(correct_operations_list_dates):
    assert src.processing.sort_by_date(*correct_operations_list_dates["input"]) == correct_operations_list_dates[
        "output"]


@pytest.mark.parametrize("incorrect_operations_list_dates", [(0), (1)], indirect=True)
def test_sort_by_incorrect_date(incorrect_operations_list_dates):
    with pytest.raises(ValueError) as exc_info:
        src.processing.sort_by_date(*incorrect_operations_list_dates["input"])

    assert str(exc_info.value) == incorrect_operations_list_dates["output"]
