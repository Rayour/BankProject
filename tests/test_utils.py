import os
from typing import Any
from unittest.mock import patch

import pytest

import src.external_api
import src.utils


@pytest.mark.parametrize("correct_data_for_mock_operation_file", [i for i in range(4)], indirect=True)
@patch("json.load")
def test_get_operations_list(mocked_file: Any, correct_data_for_mock_operation_file: Any) -> None:
    mocked_file.return_value = correct_data_for_mock_operation_file["input"]
    assert (
        src.utils.get_operations_list(os.path.join(*correct_data_for_mock_operation_file["path"]))
        == correct_data_for_mock_operation_file["output"]
    )


@pytest.mark.parametrize("transactions_list_for_sum_calculate", [i for i in range(1)], indirect=True)
@patch("src.external_api.exchange_money")
def test_get_transactions_sum(mock_exchange_money: Any, transactions_list_for_sum_calculate: Any) -> None:
    mock_exchange_money.return_value = transactions_list_for_sum_calculate["input"]["mocked_amount"]
    assert (
        src.utils.get_transactions_sum(transactions_list_for_sum_calculate["input"]["transactions"])
        == transactions_list_for_sum_calculate["output"]
    )
