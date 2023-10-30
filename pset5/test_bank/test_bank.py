from bank import value

def test_hello():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0

def test_h():
    assert value("hola") == 20
    assert value("HOLA") == 20


def test_other():
    assert value("good morning!") == 100
    assert value("GOOD MORNING!") == 100