import csv
import os.path
from pathlib import Path

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
                transactions_list.append(row)
    except Exception as ex:
        print(f"Error: {ex}")
        return []
    else:
        return transactions_list


print(read_transactions_from_csv(os.path.join('transactions.csv')))
