"""Модуль содержит функции, реализующие генераторы для обработки данных"""

from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator | Generator:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    sequence = (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )

    return sequence


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает по очереди описания операций"""

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]
        else:
            yield ""


def card_number_generator(start: int, stop: int) -> Generator:
    if not (
        isinstance(start, int)
        and isinstance(stop, int)
        and 1 <= start <= 9999999999999999
        and 1 <= stop <= 9999999999999999
    ):
        raise ValueError("Incorrect input data")

    if start < stop:
        start_gen = start
        stop_gen = stop
    else:
        start_gen = stop
        stop_gen = start

    for i in range(start_gen, stop_gen + 1):
        card_number = "0" * (16 - len(str(i))) + str(i)
        formated_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formated_card_number
