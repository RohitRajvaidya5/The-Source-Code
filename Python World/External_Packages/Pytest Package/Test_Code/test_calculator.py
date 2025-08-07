import pytest

from calculator import add, sub, mul, divide

# Basic code for pytest, just a simple test cases

def test_addition():
    assert add(6, 3) == 9
    assert add(2, 3) == 5


def test_sub():
    assert sub(2, 3) == -1
    assert sub(5, 3) == 2


def test_mul():
    assert mul(2, 3) == 6
    assert mul(2, 7) == 14


# Pytest Fixtures

@pytest.fixture
def sample_numbers():
    return 3, 4

def test_multiplication(sample_numbers):
    a, b = sample_numbers
    result = mul(a, b)
    assert result == 12

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5


# Pytest Parametrize Test

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, -1, -2)
])

def test_add_param(a, b, expected):
    assert add(a, b) == expected


# Using yield
@pytest.fixture
def open_file():
    f = open("temp.txt", "w")
    yield f
    f.close()

def test_write_file(open_file):
    open_file.write("Hello Pytest")
