"""Модуль содержит функции, позволяющие маскировать данные пользователя"""


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    correct_len_of_bank_cards = [13, 15, 16, 18, 19]

    if isinstance(card_number, int | str):
        string_card_number = str(card_number)
    else:
        raise ValueError("Incorrect card number")

    if len(string_card_number) not in correct_len_of_bank_cards:
        raise ValueError("Incorrect card number")

    if string_card_number.isdigit():
        return f"{string_card_number[0:4]} {string_card_number[4:6]}** **** {string_card_number[-4:]}"
    else:
        raise ValueError("Incorrect card number")


def get_mask_account(account: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    if isinstance(account, int | str):
        string_account = str(account)
    else:
        raise ValueError("Incorrect account number")

    if len(string_account) != 20:
        raise ValueError("Incorrect account number")

    if string_account.isdigit():
        return f"**{string_account[-4:]}"
    else:
        raise ValueError("Incorrect account number")
