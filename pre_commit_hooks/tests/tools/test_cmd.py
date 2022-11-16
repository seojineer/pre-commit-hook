import pytest
from unittest.mock import patch
import subprocess

from tools.cmd import run


@pytest.fixture
def cmd_echo_test():
    command = ["echo", "test"]
    return command

@pytest.fixture
def cmd_grep_hello():
    command = ["grep", "hello"]
    return command

def test_run(cmd_echo_test):
    expected = "test"
    ret = run(cmd_echo_test)
    assert expected in ret.stdout.decode("utf-8")
    assert 0 == ret.return_code

def test_run_raise_file_not_found():
    with pytest.raises(FileNotFoundError):
        cmd = ["nonexist", "command", "to", "run"]
        ret = run(cmd)

def test_run_with_shell():
    expected = "/usr/bin/ls"
    cmd = ["which", "ls"]
    ret = run(cmd, shell=True)
    assert expected in ret.stdout.decode("utf-8")
    assert 0 == ret.return_code

def test_run_with_input_pass(cmd_grep_hello):
    ret = run(cmd_grep_hello, input=b"hello world\n")
    assert ret.stdout == b"hello world\n"
    assert 0 == ret.return_code

def test_run_with_input_fail(cmd_grep_hello):
    ret = run(cmd_grep_hello, input=b"different text\n")
    assert ret.stdout != b"hello world\n"
    assert 1 == ret.return_code

def test_run_with_duplicated_argument(cmd_echo_test):
    with pytest.raises(TypeError):
        ret = run(cmd_echo_test, stdout=subprocess.PIPE)

def test_run_raise_type_error(cmd_echo_test):
    with pytest.raises(TypeError):
        ret = run(cmd_echo_test, dummy="nothing")
