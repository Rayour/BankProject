"""Модуль содержит функции, позволяющие работать со списком операций пользователя"""
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
