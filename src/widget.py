import masks


def mask_account_card(card_account_number: str) -> str:
    """
    Принимает строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    Для маскировки номера карты и номера счета используются разные маски.
    """

    if "Счет" in card_account_number:
        account_number = card_account_number[5:]
        masked_number = f"Счет {masks.get_mask_account(account_number)}"
    else:
        card_number = card_account_number[-16:]
        masked_number = f"{card_account_number[0:-16]}{masks.get_mask_card_number(card_number)}"

    return masked_number
