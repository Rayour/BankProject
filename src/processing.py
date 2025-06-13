"""Модуль содержит функции, позволяющие работать со списком операций пользователя"""

from datetime import date
from typing import List
import re


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


def process_bank_search(data: list[dict], search_str: str)->list[dict]:
    """Функция принимает список транзакций и строку для поиска,
    возвращает список транзакций, в которых встречается указанная строка"""

    search_result = [item for item in data if re.search(search_str, item['description'], flags=re.IGNORECASE)]
    return search_result


data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]
print(process_bank_search(data, 'сч'))