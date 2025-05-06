from typing import List


def filter_by_state(operations_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Принимает на вход список словарей с данными об операциях и статус операции.
    Значение статуса по умолчанию 'EXECUTED'
    Возвращает список операций с запрашиваемым статусом"""

    filtered_list = []

    for operation in operations_list:
        if operation["state"] == state:
            filtered_list.append(operation)

    return filtered_list
