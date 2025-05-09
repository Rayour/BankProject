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
