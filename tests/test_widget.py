import pytest

import src.widget


@pytest.mark.parametrize("correct_account_card_data", [(0), (1), (2), (3), (4), (5), (6), (7)], indirect=True)
def test_mask_account_card(correct_account_card_data):
    assert src.widget.mask_account_card(correct_account_card_data["input"]) == correct_account_card_data["output"]


@pytest.mark.parametrize("incorrect_account_card_data", [(0), (1)], indirect=True)
def test_mask_incorrect_account_card(incorrect_account_card_data):
    with pytest.raises(ValueError) as exc_info:
        src.widget.mask_account_card(incorrect_account_card_data["input"])

    assert str(exc_info.value) == incorrect_account_card_data["output"]


@pytest.mark.parametrize("correct_date_data", [(0)], indirect=True)
def test_get_date(correct_date_data):
    assert src.widget.get_date(correct_date_data["input"]) == correct_date_data["output"]


@pytest.mark.parametrize("incorrect_date_data", [(0), (1), (2)], indirect=True)
def test_get_incorrect_date(incorrect_date_data):
    with pytest.raises(ValueError) as exc_info:
        src.widget.get_date(incorrect_date_data["input"])

    assert str(exc_info.value) == incorrect_date_data["output"]
