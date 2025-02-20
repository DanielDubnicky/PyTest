import pytest
from src import calculator

def test_add():
    assert calculator.add(5,3) == 8

def test_add_wrong():
    assert calculator.test_add_wrong(5,3) == 8
