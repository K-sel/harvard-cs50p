from jar import Jar
import pytest

def test_init():
    jar = Jar()

    assert jar.capacity == 12  # capacité par défaut
    assert jar.size == 0       # jar vide au départ

    with pytest.raises(ValueError):
        Jar(0)

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    with pytest.raises(ValueError):
        assert jar.deposit(0)
    with pytest.raises(ValueError):
        assert jar.deposit(-1)
    with pytest.raises(ValueError):
        assert jar.deposit(14)


def test_withdraw():
    jar = Jar(12)
    with pytest.raises(ValueError):
        assert jar.withdraw(0)
    with pytest.raises(ValueError):
        assert jar.withdraw(13)
    with pytest.raises(ValueError):
        assert jar.withdraw(-12)
