import os.path
from typing import Any
from unittest.mock import patch

import pandas as pd
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


@pytest.mark.parametrize("transactions_from_xlsx", [i for i in range(2)], indirect=True)
@patch("pandas.read_excel")
def test_get_transactions_from_xlsx(mocked_df: Any, transactions_from_xlsx: Any) -> None:
    mocked_df.return_value = pd.DataFrame(transactions_from_xlsx["input"])
    assert src.read_data.get_transactions_from_xlsx(os.path.join('data', 'transactions_excel.xlsx')) == \
           transactions_from_xlsx["output"]


def test_get_transactions_from_xlsx_exception() -> None:
    assert src.read_data.get_transactions_from_xlsx('fake_transactions_excel.xlsx') == []
