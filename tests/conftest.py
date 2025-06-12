from typing import Any

import pytest


@pytest.fixture
def correct_card_numbers(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными номерами банковских карт
    для тестирования функции src.masks.get_mask_card_number"""

    tests = [
        {"input": "1234560123456", "output": "1234 56** **** 3456"},
        {"input": "123456890123456", "output": "1234 56** **** 3456"},
        {"input": "1234567890123456", "output": "1234 56** **** 3456"},
        {"input": "123456789012123456", "output": "1234 56** **** 3456"},
        {"input": "1234567890123123456", "output": "1234 56** **** 3456"},
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_card_numbers(request: Any) -> Any:
    """Содержит набор тестовых данных с некорректными номерами банковских карт
    для тестирования функции src.masks.get_mask_card_number"""

    tests = [
        {"input": "", "output": "Incorrect card number"},
        {"input": "123458909", "output": "Incorrect card number"},
        {"input": "djth48islg9038gj", "output": "Incorrect card number"},
        {"input": [1234567890123456], "output": "Incorrect card number"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_account_numbers(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными номерами банковских счетов
    для тестирования функции src.masks.get_mask_account"""

    tests = [{"input": "12345678901234567890", "output": "**7890"}]
    return tests[request.param]


@pytest.fixture
def incorrect_account_numbers(request: Any) -> Any:
    """Содержит набор тестовых данных с некорректными номерами банковских счетов
    для тестирования функции src.masks.get_mask_account"""

    tests = [
        {"input": "", "output": "Incorrect account number"},
        {"input": "123458909", "output": "Incorrect account number"},
        {"input": "sjtu483hltis89123456", "output": "Incorrect account number"},
        {"input": [12345678901234567890], "output": "Incorrect account number"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_account_card_data(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными данными по банковским счетам и картам
    для тестирования функции src.widgets.mask_account_card"""

    tests = [
        {"input": "Maestro 1596837868705199", "output": "Maestro 1596 83** **** 5199"},
        {"input": "Счет 64686473678894779589", "output": "Счет **9589"},
        {"input": "MasterCard 7158300734726758", "output": "MasterCard 7158 30** **** 6758"},
        {"input": "Счет 35383033474447895560", "output": "Счет **5560"},
        {"input": "Visa Classic 6831982476737658", "output": "Visa Classic 6831 98** **** 7658"},
        {"input": "Visa Platinum 8990922113665229", "output": "Visa Platinum 8990 92** **** 5229"},
        {"input": "Visa Gold 5999414228426353", "output": "Visa Gold 5999 41** **** 6353"},
        {"input": "Счет 73654108430135874305", "output": "Счет **4305"},
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_account_card_data(request: Any) -> Any:
    """Содержит набор тестовых данных с некорректными данными по банковским счетам и картам
    для тестирования функции src.widgets.mask_account_card"""

    tests = [
        {"input": "", "output": "Incorrect input data"},
        {"input": "95043734", "output": "Incorrect input data"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_date_data(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными датами
    для тестирования функции src.widgets.get_date"""

    tests = [{"input": "2024-03-11T02:26:18.671407", "output": "11.03.2024"}]
    return tests[request.param]


@pytest.fixture
def incorrect_date_data(request: Any) -> Any:
    """Содержит набор тестовых данных с некорректными датами
    для тестирования функции src.widgets.get_date"""

    tests = [
        {"input": "2024-13-11T02:26:18.671407", "output": "Incorrect input data"},
        {"input": "", "output": "Incorrect input data"},
        {"input": "MasterCard", "output": "Incorrect input data"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_operations_list_states(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными списками операций
    для тестирования функции src.processing.filter_by_state"""

    tests = [
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ],
            "output": [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        },
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                "CANCELED",
            ],
            "output": [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        },
        {
            "input": [
                [
                    {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ],
            "output": [],
        },
        {"input": [[]], "output": []},
    ]
    return tests[request.param]


@pytest.fixture
def correct_operations_list_dates(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными списками операций
    для тестирования функции src.processing.sort_by_date"""

    tests = [
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ],
            "output": [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        },
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                False,
            ],
            "output": [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        },
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ],
            "output": [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        },
        {"input": [[]], "output": []},
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_operations_list_dates(request: Any) -> Any:
    """Содержит набор тестовых данных с некорректными списками операций
    для тестирования функции src.processing.sort_by_date"""

    tests = [
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ],
            "output": "Incorrect operation date",
        },
        {
            "input": [
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-0T02:08:58.425572"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                False,
            ],
            "output": "Incorrect operation date",
        },
    ]
    return tests[request.param]


@pytest.fixture
def correct_transactions_list(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными транзакциями
    для тестирования функции src.generators.filter_by_currency"""

    input_data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-07-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-03-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    tests = [
        {
            "input": [input_data, "RUR"],
            "output": [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 939719571,
                    "state": "EXECUTED",
                    "date": "2018-07-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
        },
        {
            "input": [input_data, "USD"],
            "output": [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
        },
    ]

    return tests[request.param]


@pytest.fixture
def empty_transactions_list(request: Any) -> Any:
    """Содержит набор тестовых данных с транзакциями, дающими пустую выдачу
    для тестирования функции src.generators.filter_by_currency"""

    tests = [
        {"input": [[], "RUR"], "output": "StopIteration"},
        {
            "input": [
                [
                    {
                        "id": 142264269,
                        "state": "EXECUTED",
                        "date": "2019-03-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    }
                ],
                "EUR",
            ],
            "output": "StopIteration",
        },
    ]

    return tests[request.param]


@pytest.fixture
def correct_descriptions_transactions_list(request: Any) -> Any:
    """Содержит набор тестовых данных с корректными транзакциями и описаниями
    для тестирования функции src.generators.transaction_descriptions"""

    input_data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-07-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUR", "code": "RUR"}},
            "description": "",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-03-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    tests = [
        {
            "input": input_data,
            "output": [
                "Перевод организации",
                "Перевод со счета на счет",
                "",
                "",
            ],
        }
    ]

    return tests[request.param]


@pytest.fixture
def empty_descriptions_transactions_list(request: Any) -> Any:
    """Содержит пустой список транзакций
    для тестирования функции src.generators.transaction_descriptions"""

    tests = [{"input": [], "output": "StopIteration"}]

    return tests[request.param]


@pytest.fixture
def correct_input_data_card_number_generator(request: Any) -> Any:
    """Содержит корректный набор данных для генерации номеров банковских карт
    для тестирования функции src.generators.card_number_generator"""

    tests = [
        {"input": [1, 3], "output": ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]},
        {
            "input": [9876543298765432, 9876543298765430],
            "output": ["9876 5432 9876 5430", "9876 5432 9876 5431", "9876 5432 9876 5432"],
        },
    ]

    return tests[request.param]


@pytest.fixture
def incorrect_input_data_card_number_generator(request: Any) -> Any:
    """Содержит некорректный набор данных для генерации номеров банковских карт
    для тестирования функции src.generators.card_number_generator"""

    tests = [
        {"input": ["as", 6], "output": "Incorrect input data"},
        {"input": [5, "as"], "output": "Incorrect input data"},
        {"input": [-2, 123], "output": "Incorrect input data"},
        {"input": [123, -2], "output": "Incorrect input data"},
    ]

    return tests[request.param]


@pytest.fixture
def log_decoration(request: Any) -> Any:
    """Содержит набор данных для тестирования декоратора логирования
    src.decorators.log"""
    tests = [
        {"input": (3, 5), "output": "[INFO] Function sum_a_b([(3, 5), {}]) successfully finished at with result 8\n"},
        {
            "input": ("a", 5),
            "output": """[ERROR] Function sum_a_b([('a', 5), {}]) failed at with error "unsupported operand type(s) \
for +: 'int' and 'str'"\n""",
        },
    ]

    return tests[request.param]


@pytest.fixture
def correct_data_for_mock_operation_file(request: Any) -> Any:
    """Содержит данные для тестирования функции src.utils.get_operations_list"""

    tests = [
        {
            "input": [
                {
                    "id": 667307132,
                    "state": "EXECUTED",
                    "date": "2019-07-13T18:51:29.313309",
                    "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод с карты на счет",
                    "from": "Maestro 1308795367077170",
                    "to": "Счет 96527012349577388612",
                }
            ],
            "output": [
                {
                    "id": 667307132,
                    "state": "EXECUTED",
                    "date": "2019-07-13T18:51:29.313309",
                    "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод с карты на счет",
                    "from": "Maestro 1308795367077170",
                    "to": "Счет 96527012349577388612",
                }
            ],
            "path": ("data", "operations.json"),
        },
        {"input": [], "output": [], "path": ("data", "operations.json")},
        {"input": "some string", "output": [], "path": ("data", "operations.json")},
        {"input": "some string", "output": [], "path": ("fake_file.json",)},
    ]

    return tests[request.param]


@pytest.fixture
def correct_exchange_money_data_for_mock(request: Any) -> Any:
    """Содержит данные для позитивного тестирования функции src.external_api.exchange_money"""

    tests = [{"input": {"status": 200, "json": {"result": 3724.305775, "success": True}}, "output": 3724.305775}]

    return tests[request.param]


@pytest.fixture
def incorrect_exchange_money_data_for_mock(request: Any) -> Any:
    """Содержит данные для тестирования исключений функции src.external_api.exchange_money"""

    tests = [
        {
            "input": {"status": 200, "json": {"result": 3724.305775, "success": False}},
            "output": "Something went wrong, try later",
        },
        {
            "input": {
                "status": 200,
                "json": {
                    "result": 3724.305775,
                },
            },
            "output": "Something went wrong, try later",
        },
        {"input": {"status": 200, "json": None}, "output": "Something went wrong, try later"},
        {"input": {"status": 500, "json": {}}, "output": "Something went wrong, try later"},
    ]

    return tests[request.param]


@pytest.fixture
def transactions_list_for_sum_calculate(request: Any) -> Any:
    """Содержит данные для тестирования функции src.utils.get_transactions_sum"""

    tests = [
        {
            "input": {
                "transactions": [
                    {
                        "id": 441945886,
                        "state": "EXECUTED",
                        "date": "2019-08-26T10:50:58.294041",
                        "operationAmount": {"amount": "30000.52", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Maestro 1596837868705199",
                        "to": "Счет 64686473678894779589",
                    },
                    {
                        "id": 41428829,
                        "state": "EXECUTED",
                        "date": "2019-07-03T18:35:29.512364",
                        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "MasterCard 7158300734726758",
                        "to": "Счет 35383033474447895560",
                    },
                ],
                "mocked_amount": 20000.51,
            },
            "output": 50001.03,
        }
    ]

    return tests[request.param]


@pytest.fixture
def transactions_list_for_read_from_csv(request: Any) -> Any:
    """Содержит данные для мока csv файла для теста функции src.read_data.read_transactions_from_csv"""

    tests = [
        {
            "input": [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
                       'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                       'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                      {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
                       'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                       'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}],

            "output": [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
                        'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                        'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                       {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
                        'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                        'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}],
        },
        {
            "input": [],

            "output": [],
        }
    ]

    return tests[request.param]


@pytest.fixture
def transactions_from_xlsx(request: Any) -> Any:
    """Содержит данные для мока xlsx файла для теста функции src.read_data.read_transactions_from_xlsx"""

    tests = [
        {
            "input": {'id': [650703, 3598919], 'state': ['EXECUTED', 'EXECUTED'],
                      'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'], 'amount': [16210.0, 29740.0],
                      'currency_name': ['Sol', 'Peso'], 'currency_code': ['PEN', 'COP'],
                      'from': ['Счет 58803664561298323391', 'Discover 3172601889670065'],
                      'to': ['Счет 39745660563456619397', 'Discover 0720428384694643'],
                      'description': ['Перевод организации', 'Перевод с карты на карту']},
            "output": [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210.0',
                        'currency_name': 'Sol',
                        'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                        'description': 'Перевод организации'},
                       {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                        'amount': '29740.0', 'currency_name': 'Peso', 'currency_code': 'COP',
                        'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
                        'description': 'Перевод с карты на карту'}]
        },
        {
            "input": {'id': [], 'state': [],
                      'date': [], 'amount': [],
                      'currency_name': [], 'currency_code': [],
                      'from': [],
                      'to': [],
                      'description': []},
            "output": []
        }
    ]

    return tests[request.param]
