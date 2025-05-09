from typing import Any

import pytest

import src.generators


@pytest.mark.parametrize("correct_transactions_list", [i for i in range(2)], indirect=True)
def test_filter_by_currency(correct_transactions_list: Any) -> None:
    gen = src.generators.filter_by_currency(*correct_transactions_list["input"])
    for j in range(len(correct_transactions_list["output"])):
        assert next(gen) == correct_transactions_list["output"][j]


@pytest.mark.parametrize("empty_transactions_list", [i for i in range(2)], indirect=True)
def test_filter_by_currency_empty(empty_transactions_list: Any) -> None:

    gen = src.generators.filter_by_currency(*empty_transactions_list["input"])
    with pytest.raises(StopIteration) as exc_info:
        next(gen)

    assert str(exc_info.typename) == empty_transactions_list["output"]


@pytest.mark.parametrize("correct_descriptions_transactions_list", [i for i in range(1)], indirect=True)
def test_transaction_descriptions(correct_descriptions_transactions_list: Any) -> None:
    gen = src.generators.transaction_descriptions(correct_descriptions_transactions_list["input"])
    for j in range(len(correct_descriptions_transactions_list["output"])):
        assert next(gen) == correct_descriptions_transactions_list["output"][j]


@pytest.mark.parametrize("empty_descriptions_transactions_list", [i for i in range(1)], indirect=True)
def test_transaction_descriptions_empty(empty_descriptions_transactions_list: Any) -> None:

    gen = src.generators.transaction_descriptions(empty_descriptions_transactions_list["input"])
    with pytest.raises(StopIteration) as exc_info:
        next(gen)

    assert str(exc_info.typename) == empty_descriptions_transactions_list["output"]
