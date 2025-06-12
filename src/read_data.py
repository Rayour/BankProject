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
                    row['id'] = int(row['id'])
                    transactions_list.append(row)
    except Exception as ex:
        print(f"Error: {ex}")
        return []
    else:
        return transactions_list


def get_transactions_from_xlsx(xlsx_path: str) -> list[dict] | Any:
    """Функция получает на вход путь до xlsx файла с транзакциями,
    возвращает список транзакций"""

    full_xlsx_path = os.path.join(ROOT_PATH, xlsx_path)

    try:
        transactions_df = pd.read_excel(full_xlsx_path)
        not_empty_transactions_df = transactions_df.loc[transactions_df.id.notnull()]
        not_empty_transactions_df.id = not_empty_transactions_df.id.map(int)
        not_empty_transactions_df.amount = not_empty_transactions_df.amount.map(str)
        transactions_list = json.loads(not_empty_transactions_df.to_json(orient='records'))
    except Exception as ex:
        print(f"Error: {ex}")
        return []
    else:
        return transactions_list
