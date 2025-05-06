"""Модуль содержит функции, позволяющие маскировать данные пользователя"""


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    string_card_number = str(card_number)
    return f"{string_card_number[0:4]} {string_card_number[4:6]}** **** {string_card_number[-4:]}"


def get_mask_account(account: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    string_account = str(account)
    return f"**{string_account[-4:]}"
