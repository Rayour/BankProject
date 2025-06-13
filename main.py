import os

from src import generators, processing, read_data, utils, widget

# Получаем информацию об источнике транзакций
while True:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
    transactions_source = input()
    print()

    if transactions_source in ["1", "2", "3"]:
        break
    else:
        print("Выбран некорректный источник о транзакциях. Пожалуйста, укажите 1, 2 или 3.")
        print()

# Получаем список транзакций из источника
if transactions_source == "1":
    print("Для обработки выбран JSON-файл.")
    transactions = utils.get_operations_list(os.path.join(os.getcwd(), "data", "operations.json"))
elif transactions_source == "2":
    print("Для обработки выбран CSV-файл.")
    transactions = read_data.read_transactions_from_csv(os.path.join(os.getcwd(), "data", "transactions.csv"))
else:
    print("Для обработки выбран XLSX-файл.")
    transactions = read_data.read_transactions_from_xlsx(os.path.join(os.getcwd(), "data", "transactions_excel.xlsx"))

print()

# Получаем информацию о статусе транзакций
while True:
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    status = input().upper()
    print()

    if status in ["EXECUTED", "CANCELED", "PENDING"]:
        break
    else:
        print("Введен некорректный статус.")
        print()

# Фильтруем транзакции по указанному статусу
transactions = processing.filter_by_state(transactions, status)

# Запрос необходимости сортировки по дате
while True:
    print("Отсортировать операции по дате? Да/Нет")
    is_sort_by_date = input().lower()
    print()

    if is_sort_by_date in ["да", "нет"]:
        break
    else:
        print("Введен некорректный ответ")
        print()

# Запрос направления сортировки по дате и сортировка
if is_sort_by_date == "да":
    while True:
        print("""Отсортировать по:
         1. Возрастанию
         2. Убыванию""")
        asc_desc = input()
        print()

        if asc_desc in ["1", "2"]:
            break
        else:
            print("Указано некорректное направление сортировки. Пожалуйста, укажите 1, или 2.")
            print()

    if asc_desc == "1":
        sort_revert = False
    else:
        sort_revert = True

    transactions = processing.sort_by_date(transactions, sort_reverse=sort_revert)

# Запрос на вывод рублевых транзакций
while True:
    print("Выводить только рублевые транзакции? Да/Нет")
    is_rub_only = input().lower()
    print()

    if is_rub_only in ["да", "нет"]:
        break
    else:
        print("Введен некорректный ответ")
        print()

# Фильтрация по валюте
if is_rub_only == "да":
    transactions = list(generators.filter_by_currency(transactions, "RUB"))

# Запрос на фильтрацию по подстроке в описании
while True:
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    is_search = input().lower()
    print()

    if is_search in ["да", "нет"]:
        break
    else:
        print("Введен некорректный ответ")
        print()

# Фильтрация по подстроке в описании
if is_search == "да":
    search_str = input("Укажите слово для поиска: ")
    print()
    transactions = processing.process_bank_search(transactions, search_str)

# Вывод результата
print("Распечатываю итоговый список транзакций...")
print()
print(f"Всего банковских операций в выборке: {len(transactions)}")
print()
for item in transactions:
    operation_date = widget.get_date(item["date"])
    operation_from = widget.mask_account_card(item["from"])
    operation_to = widget.mask_account_card(item["to"])
    operation_currency = item["operationAmount"]["currency"]["name"]
    print(f"{operation_date} {item["description"]}")
    print(f"{operation_from} -> {operation_to}")
    print(f"Сумма: {item["operationAmount"]["amount"]} {operation_currency}")
    print()
