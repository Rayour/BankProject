import pytest

import src.masks


@pytest.mark.parametrize("correct_card_numbers", [(0), (1), (2), (3), (4)], indirect=True)
def test_get_mask_card_number(correct_card_numbers: dict) -> None:
    assert src.masks.get_mask_card_number(correct_card_numbers["input"]) == correct_card_numbers["output"]


@pytest.mark.parametrize("incorrect_card_numbers", [(0), (1), (2), (3)], indirect=True)
def test_get_mask_card_incorrect_number(incorrect_card_numbers: dict) -> None:
    with pytest.raises(ValueError) as exc_info:
        src.masks.get_mask_card_number(incorrect_card_numbers["input"])

    assert str(exc_info.value) == incorrect_card_numbers["output"]


@pytest.mark.parametrize("correct_account_numbers", [(0)], indirect=True)
def test_get_mask_account(correct_account_numbers: dict) -> None:
    assert src.masks.get_mask_account(correct_account_numbers["input"]) == correct_account_numbers["output"]


@pytest.mark.parametrize("incorrect_account_numbers", [(0), (1), (2), (3)], indirect=True)
def test_get_mask_incorrect_account(incorrect_account_numbers: dict) -> None:
    with pytest.raises(ValueError) as exc_info:
        src.masks.get_mask_account(incorrect_account_numbers["input"])

    assert str(exc_info.value) == incorrect_account_numbers["output"]
