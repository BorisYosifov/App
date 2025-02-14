import pytest
from fizzbuzz import fizzbuzz  # Импортиране на функцията (която предстои да се напише)

def test_returns_number():
    simple_number = 1  # Избягване на "магически числа"
    assert fizzbuzz(simple_number) == simple_number  # Очакваме 1 да върне 1
