import os.path
from typing import Any
from unittest.mock import patch

import pytest

import src.read_data


@pytest.mark.parametrize("transactions_list_for_read_from_csv", [i for i in range(2)], indirect=True)
@patch("csv.DictReader")
def test_get_transactions_from_csv(mocked_file: Any, transactions_list_for_read_from_csv: Any) -> None:
    mocked_file.return_value = transactions_list_for_read_from_csv["input"]
    assert src.read_data.read_transactions_from_csv(os.path.join('data', 'transactions.csv')) == \
           transactions_list_for_read_from_csv["output"]


def test_get_transactions_from_csv_exception() -> None:
    assert src.read_data.read_transactions_from_csv('fake_transactions.csv') == []
