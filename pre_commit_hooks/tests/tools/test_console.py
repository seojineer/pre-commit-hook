import pytest
from unittest.mock import patch
import io

from tools.console import Console as cs


@pytest.fixture
def test_message():
    return "pineapple"

@pytest.fixture
def default_error_strig(test_message):
    return f"{cs._bold}{cs._red}{test_message}{cs._reset}"

def test_console_error(test_message):
    with patch('sys.stdout', new_callable=io.StringIO) as stdout:
        cs.error(test_message)
        ret = stdout.getvalue()
        assert test_message != ret
        assert test_message in ret
