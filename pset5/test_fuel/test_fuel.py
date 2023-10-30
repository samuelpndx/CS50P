from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50

    with pytest.raises(ValueError):
        convert("cat")
        convert("cat/1")
        convert("1/cat")
        convert("two/one")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("21")
    with pytest.raises(ValueError):
        convert("3.14/4")
        convert("2/3.14")
    with pytest.raises(ValueError):
        convert("-1/2")
        convert("1/-2")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"