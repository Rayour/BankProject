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


@pytest.mark.parametrize("correct_input_data_card_number_generator", [i for i in range(2)], indirect=True)
def test_card_number_generator(correct_input_data_card_number_generator: Any) -> None:
    gen = src.generators.card_number_generator(*correct_input_data_card_number_generator["input"])
    for j in range(len(correct_input_data_card_number_generator["output"])):
        assert next(gen) == correct_input_data_card_number_generator["output"][j]


@pytest.mark.parametrize("incorrect_input_data_card_number_generator", [i for i in range(4)], indirect=True)
def test_card_number_generator_incorrect(incorrect_input_data_card_number_generator: Any) -> None:

    gen = src.generators.card_number_generator(*incorrect_input_data_card_number_generator["input"])
    with pytest.raises(ValueError) as exc_info:
        next(gen)

    assert str(exc_info.value) == incorrect_input_data_card_number_generator["output"]
