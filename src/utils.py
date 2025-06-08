import json
import os
from pathlib import Path


def get_operations_list(path_to_json: str) -> list[dict]:
    """Получает на вход путь до json файла, возвращает список словарей с информацией об операциях"""

    PATH_TO_JSON = os.path.join(Path(__file__).resolve().parents[1], path_to_json)

    try:
        with open(PATH_TO_JSON, "r", encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            if isinstance(operations_list, list) and operations_list:
                return operations_list
            else:
                return []
    except FileNotFoundError:
        print("En error occurred. File not found. Please, check the file or path and try again.")
        return []
