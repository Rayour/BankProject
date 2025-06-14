import pytest

import src.widget


@pytest.mark.parametrize("correct_account_card_data", [i for i in range(9)], indirect=True)
def test_mask_account_card(correct_account_card_data: dict) -> None:
    assert src.widget.mask_account_card(correct_account_card_data["input"]) == correct_account_card_data["output"]


@pytest.mark.parametrize("incorrect_account_card_data", [i for i in range(1)], indirect=True)
def test_mask_incorrect_account_card(incorrect_account_card_data: dict) -> None:
    with pytest.raises(ValueError) as exc_info:
        src.widget.mask_account_card(incorrect_account_card_data["input"])

    assert str(exc_info.value) == incorrect_account_card_data["output"]


@pytest.mark.parametrize("correct_date_data", [i for i in range(1)], indirect=True)
def test_get_date(correct_date_data: dict) -> None:
    assert src.widget.get_date(correct_date_data["input"]) == correct_date_data["output"]


@pytest.mark.parametrize("incorrect_date_data", [i for i in range(3)], indirect=True)
def test_get_incorrect_date(incorrect_date_data: dict) -> None:
    with pytest.raises(ValueError) as exc_info:
        src.widget.get_date(incorrect_date_data["input"])

    assert str(exc_info.value) == incorrect_date_data["output"]
