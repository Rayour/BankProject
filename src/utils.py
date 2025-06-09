import json
import os
from pathlib import Path

from src.external_api import exchange_money


def get_operations_list(path_to_json: str) -> list[dict]:
    """Получает на вход путь до json файла, возвращает список словарей с информацией об операциях"""

    PATH_TO_JSON = os.path.join(Path(__file__).resolve().parents[1], path_to_json)

    try:
        with open(PATH_TO_JSON, "r", encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            if isinstance(operations_list, list) and operations_list:
                return operations_list
            else:
                return []
    except FileNotFoundError:
        print("En error occurred. File not found. Please, check the file or path and try again.")
        return []


def get_transactions_sum(transactions: list[dict]) -> float:
    """Получает на вход список словарей с транзакциями, возвращает сумму всех транзакций в рублях.
    Конвертация из других валют происходит по текущему курсу на момент расчетов"""

    transactions_sum = 0.0

    for transaction in transactions:
        print(transaction)
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            transactions_sum += float(transaction["operationAmount"]["amount"])
        else:
            amount_rub = exchange_money(
                transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
            )
            transactions_sum += float(amount_rub)

    return transactions_sum
