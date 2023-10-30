from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(2)
    assert jar.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    jar.deposit(6)
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0