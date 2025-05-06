import pytest

import src.masks
from src import masks


@pytest.mark.parametrize('number, expected', [
    ("1234567890123456", "1234 56** **** 3456"),
    ("", "Incorrect card number"),
    ("djth48islg9038gj", "Incorrect card number")
])
def test_get_mask_card_number(number, expected):
    assert src.masks.get_mask_card_number(number) == expected


@pytest.mark.parametrize('number, expected', [
    ("12345678901234567890", "**7890"),
    ("", "Incorrect account number"),
    ("djth48islg9038gj", "Incorrect account number")
])
def test_get_mask_account(number, expected):
    assert src.masks.get_mask_account(number) == expected
