"""Модуль содержит функции, позволяющие работать со списком операций пользователя"""

import re
from collections import Counter, defaultdict
from datetime import date
from typing import List


def filter_by_state(operations_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Принимает на вход список словарей с данными об операциях и статус операции.
    Значение статуса по умолчанию 'EXECUTED'
    Возвращает список операций с запрашиваемым статусом"""

    filtered_list = []

    for operation in operations_list:
        print(operation)
        if "state" in operation.keys() and operation["state"] == state:
            filtered_list.append(operation)

    return filtered_list


def sort_by_date(operations_list: List[dict], sort_reverse: bool = True) -> List[dict]:
    """Функция получает на вход список операций и сортирует их по дате в указанном направлении.
    По умолчанию сортировка происходит по убыванию"""

    for operation in operations_list:
        try:
            date.fromisoformat(operation["date"][:10])
        except Exception:
            raise ValueError("Incorrect operation date")

    return sorted(operations_list, key=lambda x: x["date"], reverse=sort_reverse)


def process_bank_search(transactions: list[dict], search_str: str) -> list[dict]:
    """Функция принимает список транзакций и строку для поиска,
    возвращает список транзакций, в описании которых встречается указанная строка"""

    search_result = [item for item in transactions if re.search(search_str, item['description'], flags=re.IGNORECASE)]
    return search_result


def get_count_process_bank_operations_categories(transactions: list[dict], categories: list) -> dict:
    """Функция принимает список транзакций и список категорий,
    возвращает словарь с количеством транзакций каждой запрашиваемой категории"""

    transactions_categories = [item["description"] for item in transactions]
    counted_categories = Counter(transactions_categories)
    result = defaultdict(int)

    for category in categories:
        if category in counted_categories:
            result[category] = counted_categories[category]
        else:
            result[category] = 0

    return result
