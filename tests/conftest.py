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
