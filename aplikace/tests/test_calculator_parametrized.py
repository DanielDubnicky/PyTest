import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0, 5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0, 5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0, 0) == 0

@pytest.mark.parametrize(
    "a, b, exptected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)

def test_add_parametrized(a, b, exptected):
    assert calculator.add_wrong(a, b) == exptected

@pytest.mark.parametrize(

    "a, b, expected_exception, expected_msg",
    [

        (8, 5, ValueError, "Cannot take log of non-positive number!"),

        (-2, 5, ValueError, "Cannot take log of non-positive number)"),

        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),

        (5, 1, NameError, "Cannot take log with base 1!"),
    ],

)

def test_log(a, b, expected_exception, expected_msg): 
    with pytest.raises(expected_exception) as exc: 
        calculator.log(a, b)