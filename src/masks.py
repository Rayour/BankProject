"""Модуль содержит функции, позволяющие маскировать данные пользователя"""

import datetime
import logging
import os
from pathlib import Path

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
    encoding="utf-8",
)
logger = logging.getLogger("masks")


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    correct_len_of_bank_cards = [13, 15, 16, 18, 19]

    if isinstance(card_number, int | str):
        string_card_number = str(card_number)
    else:
        logger.critical(f"Некорректный номер карты: {card_number}")
        raise ValueError("Incorrect card number")

    if len(string_card_number) not in correct_len_of_bank_cards:
        logger.critical(f"Некорректный номер карты: {card_number}")
        raise ValueError("Incorrect card number")

    if string_card_number.isdigit():
        mask_account = f"{string_card_number[0:4]} {string_card_number[4:6]}** **** {string_card_number[-4:]}"
        logger.info(f"Для номера карты {card_number} сгенерирована маска {mask_account}")
        return mask_account
    else:
        logger.critical(f"Некорректный номер карты: {card_number}")
        raise ValueError("Incorrect card number")


def get_mask_account(account: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    if isinstance(account, int | str):
        string_account = str(account)
    else:
        logger.critical(f"Некорректный номер счета: {account}")
        raise ValueError("Incorrect account number")

    if len(string_account) != 20:
        logger.critical(f"Некорректный номер счета: {account}")
        raise ValueError("Incorrect account number")

    if string_account.isdigit():
        logger.info(f"Для счета {account} сгенерирована маска **{string_account[-4:]}")
        return f"**{string_account[-4:]}"
    else:
        logger.critical(f"Некорректный номер счета: {account}")
        raise ValueError("Incorrect account number")
