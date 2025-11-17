import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(3)
    assert jar2.capacity == 3

    # invalid capacities
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(3.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    # over capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

    # negative / invalid amounts
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    # more than available
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # negative / invalid amounts
    with pytest.raises(ValueError):
        jar.withdraw(-2)
