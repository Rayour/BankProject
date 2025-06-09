from typing import Any
from unittest.mock import patch

import pytest

import src.external_api


@pytest.mark.parametrize("correct_exchange_money_data_for_mock", [i for i in range(1)], indirect=True)
@patch("requests.get")
def test_exchange_money(mocked_get: Any, correct_exchange_money_data_for_mock: Any) -> None:
    mocked_get.return_value.json.return_value = correct_exchange_money_data_for_mock["input"]["json"]
    mocked_get.return_value.status_code = correct_exchange_money_data_for_mock["input"]["status"]
    assert src.external_api.exchange_money("5", "USD") == correct_exchange_money_data_for_mock["output"]


@pytest.mark.parametrize("incorrect_exchange_money_data_for_mock", [i for i in range(4)], indirect=True)
@patch("requests.get")
def test_exchange_money_exception(mocked_get: Any, incorrect_exchange_money_data_for_mock: Any) -> None:
    mocked_get.return_value.json.return_value = incorrect_exchange_money_data_for_mock["input"]["json"]
    mocked_get.return_value.status_code = incorrect_exchange_money_data_for_mock["input"]["status"]

    with pytest.raises(Exception) as exc_info:
        src.external_api.exchange_money("5", "USD")

    assert str(exc_info.value) == incorrect_exchange_money_data_for_mock["output"]
