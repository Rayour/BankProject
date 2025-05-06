"""Модуль содержит функции, позволяющие маскировать данные пользователя"""


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    if isinstance(card_number, int | str):
        string_card_number = str(card_number)
    else:
        return "Incorrect card number"

    if len(string_card_number) != 16:
        return "Incorrect card number"

    if string_card_number.isdigit():
        return f"{string_card_number[0:4]} {string_card_number[4:6]}** **** {string_card_number[-4:]}"
    else:
        return "Incorrect card number"


def get_mask_account(account: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    if isinstance(account, int | str):
        string_account = str(account)
    else:
        return "Incorrect account number"

    if len(string_account) != 20:
        return "Incorrect account number"

    if string_account.isdigit():
        return f"**{string_account[-4:]}"
    else:
        return "Incorrect account number"
