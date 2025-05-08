"""Модуль содержит функции, позволяющие обрабатывать данные пользователя"""

from datetime import date

import src.masks


def mask_account_card(card_account_number: str) -> str:
    """
    Принимает строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    Для маскировки номера карты и номера счета используются разные маски.
    """

    if "Счет" in card_account_number:
        account_number = card_account_number[5:]
        masked_number = f"Счет {src.masks.get_mask_account(account_number)}"
    else:
        first_char_of_number = 0

        for i in range(len(card_account_number)):
            if card_account_number[i].isdigit():
                card_number = card_account_number[i:]
                first_char_of_number = i
                break

        if first_char_of_number == 0:
            raise ValueError("Incorrect input data")

        masked_number = f"{card_account_number[0:first_char_of_number]}{src.masks.get_mask_card_number(card_number)}"

    return masked_number


def get_date(date_string: str) -> str:
    """Принимает на вход дату в формате ISO строки, отдает дату в формате ДД.ММ.ГГГГ"""

    try:
        date.fromisoformat(date_string[:10])
        return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"
    except ValueError:
        raise ValueError("Incorrect input data")
