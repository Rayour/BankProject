import pytest


@pytest.fixture
def correct_card_numbers(request):
    """Содержит набор тестовых данных с корректными номерами банковских карт"""

    tests = [
        {"input": "1234560123456", "output": "1234 56** **** 3456"},
        {"input": "123456890123456", "output": "1234 56** **** 3456"},
        {"input": "1234567890123456", "output": "1234 56** **** 3456"},
        {"input": "123456789012123456", "output": "1234 56** **** 3456"},
        {"input": "1234567890123123456", "output": "1234 56** **** 3456"},
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_card_numbers(request):
    """Содержит набор тестовых данных с некорректными номерами банковских карт"""

    tests = [
        {"input": "", "output": "Incorrect card number"},
        {"input": "123458909", "output": "Incorrect card number"},
        {"input": "djth48islg9038gj", "output": "Incorrect card number"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_account_numbers(request):
    """Содержит набор тестовых данных с корректными номерами банковских счетов"""

    tests = [
        {"input": "12345678901234567890", "output": "**7890"}
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_account_numbers(request):
    """Содержит набор тестовых данных с некорректными номерами банковских счетов"""

    tests = [
        {"input": "", "output": "Incorrect account number"},
        {"input": "123458909", "output": "Incorrect account number"},
        {"input": "sjtu483hltis8912345", "output": "Incorrect account number"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_account_card_data(request):
    """Содержит набор тестовых данных с корректными данными по банковским счетам и картам"""

    tests = [
        {"input": "Maestro 1596837868705199", "output": "Maestro 1596 83** **** 5199"},
        {"input": "Счет 64686473678894779589", "output": "Счет **9589"},
        {"input": "MasterCard 7158300734726758", "output": "MasterCard 7158 30** **** 6758"},
        {"input": "Счет 35383033474447895560", "output": "Счет **5560"},
        {"input": "Visa Classic 6831982476737658", "output": "Visa Classic 6831 98** **** 7658"},
        {"input": "Visa Platinum 8990922113665229", "output": "Visa Platinum 8990 92** **** 5229"},
        {"input": "Visa Gold 5999414228426353", "output": "Visa Gold 5999 41** **** 6353"},
        {"input": "Счет 73654108430135874305", "output": "Счет **4305"}
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_account_card_data(request):
    """Содержит набор тестовых данных с некорректными данными по банковским счетам и картам"""

    tests = [
        {"input": "", "output": "Incorrect input data"},
        {"input": "95043734", "output": "Incorrect input data"},
    ]
    return tests[request.param]


@pytest.fixture
def correct_date_data(request):
    """Содержит набор тестовых данных с корректными датами"""

    tests = [
        {"input": "2024-03-11T02:26:18.671407", "output": "11.03.2024"}
    ]
    return tests[request.param]


@pytest.fixture
def incorrect_date_data(request):
    """Содержит набор тестовых данных с некорректными датами"""

    tests = [
        {"input": "2024-13-11T02:26:18.671407", "output": "Incorrect input data"},
        {"input": "", "output": "Incorrect input data"},
        {"input": "MasterCard", "output": "Incorrect input data"}
    ]
    return tests[request.param]
