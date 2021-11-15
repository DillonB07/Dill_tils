import pytest
from dill_tils.text import write, clear


def test_write():
    output = write("Hello World")
    assert output == True


def test_clear():
    output = clear()
    assert output == True
