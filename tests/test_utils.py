import os
from typing import Any
from unittest.mock import patch

import pytest

import src.utils


@pytest.mark.parametrize("correct_data_for_mock_operation_file", [i for i in range(4)], indirect=True)
@patch('json.load')
def test_get_operations_list(mocked_file: Any, correct_data_for_mock_operation_file: Any) -> None:
    mocked_file.return_value = correct_data_for_mock_operation_file["input"]
    assert src.utils.get_operations_list(os.path.join(*correct_data_for_mock_operation_file["path"])) == \
           correct_data_for_mock_operation_file["output"]
