import datetime
import json
import logging
import os
from pathlib import Path

import src.external_api

ROOT_PATH = Path(__file__).resolve().parents[1]
date_today = datetime.datetime.today().strftime("%d-%m-%Y")
file_name = f"{date_today}_logs.log"
log_path = os.path.join(ROOT_PATH, "logs", file_name)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=log_path,
    filemode="w",
    encoding='utf-8'
)
logger = logging.getLogger("utils")


def get_operations_list(path_to_json: str) -> list[dict]:
    """Получает на вход путь до json файла, возвращает список словарей с информацией об операциях"""

    PATH_TO_JSON = os.path.join(ROOT_PATH, path_to_json)

    try:
        logger.info(f"Попытка чтения файла {PATH_TO_JSON}")
        with open(PATH_TO_JSON, "r", encoding="utf-8") as json_file:
            logger.info(f"Получение JSON из файла {PATH_TO_JSON}")
            operations_list = json.load(json_file)
            if isinstance(operations_list, list) and operations_list:
                logger.info(f"Успешно получен JSON из файла {PATH_TO_JSON}")
                return operations_list
            else:
                logger.warning(f"Некорректные данные в файле {PATH_TO_JSON}. Получен пустой список транзакций.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {PATH_TO_JSON} не найден. Получен пустой список транзакций.")
        return []


def get_transactions_sum(transactions: list[dict]) -> float:
    """Получает на вход список словарей с транзакциями, возвращает сумму всех транзакций в рублях.
    Конвертация из других валют происходит по текущему курсу на момент расчетов"""

    transactions_sum = 0.0

    for transaction in transactions:
        logger.info(f"Начало обработки транзакции {transaction}")
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Транзакция в рублях, конвертация не требуется")
            transactions_sum += float(transaction["operationAmount"]["amount"])
        else:
            logger.info(f"Транзакция в {transaction["operationAmount"]["currency"]["code"]}, запрос конвертации.")
            amount_rub = src.external_api.exchange_money(
                transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
            )
            transactions_sum += amount_rub
    logger.info(f"Сумма транзакций в рублях: {transactions_sum}")
    return transactions_sum

print(get_operations_list(os.path.join(ROOT_PATH, 'data', 'operations.json')))