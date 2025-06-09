import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def exchange_money(amount_currency: float, currency_from_convert: str) -> float | Any:
    """Получает на вход сумму в рублях и валюту для конвертации,
    возвращает сумму в указанной валюте"""

    exchange_service_api_key = os.getenv("EXCHANGE_SERVICE_API_KEY")
    headers = {"apikey": exchange_service_api_key}
    params = {"to": "RUB", "from": currency_from_convert, "amount": str(amount_currency)}

    response = requests.get("https://api.apilayer.com/exchangerates_data/convert", headers=headers, params=params)

    if (
        response.status_code == 200
        and response.json()
        and ("success" in response.json())
        and response.json()["success"]
    ):
        return response.json()["result"]
    else:
        raise Exception("Something went wrong, try later")
