import csv
import json
import os.path
from pathlib import Path
from typing import Any

import pandas as pd

ROOT_PATH = Path(__file__).resolve().parents[1]


def read_transactions_from_csv(csv_path: str) -> list[dict]:
    """Функция получает на вход путь до csv файла с транзакциями,
    возвращает список транзакций"""

    full_csv_path = os.path.join(ROOT_PATH, csv_path)
    transactions_list = []

    try:
        with open(full_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row['id']:
                    new_row = {
                        'id': int(row['id']),
                        'state': row['state'],
                        'date': row['date'],
                        'description': row['description'],
                        'operationAmount': {
                            "amount": row['amount'],
                            "currency": {
                                "name": row['currency_name'],
                                "code": row['currency_code']
                            }
                        },
                        'to': row['to'],
                        'from': row['from']
                    }
                    transactions_list.append(new_row)
    except Exception as ex:
        print(f"Error: {ex}")
        return []
    else:
        return transactions_list


def read_transactions_from_xlsx(xlsx_path: str) -> list[dict]:
    """Функция получает на вход путь до xlsx файла с транзакциями,
    возвращает список транзакций"""

    full_xlsx_path = os.path.join(ROOT_PATH, xlsx_path)

    try:
        transactions_df = pd.read_excel(full_xlsx_path)
        not_empty_transactions_df = transactions_df.loc[transactions_df.id.notnull()]
        transactions_list = json.loads(not_empty_transactions_df.to_json(orient='records'))
        formated_transactions_list = []
        for transaction in transactions_list:
            formated_transaction = {
                                        'id': int(transaction['id']),
                                        'state': transaction['state'],
                                        'date': transaction['date'],
                                        'description': transaction['description'],
                                        'operationAmount': {
                                            "amount": str(transaction['amount']),
                                            "currency": {
                                                "name": transaction['currency_name'],
                                                "code": transaction['currency_code']
                                            }
                                        },
                                        'to': transaction['to'],
                                        'from': transaction['from']
                                    }
            formated_transactions_list.append(formated_transaction)
    except Exception as ex:
        print(f"Error: {ex}")
        return []
    else:
        return formated_transactions_list
