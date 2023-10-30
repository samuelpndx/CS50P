from working import convert
import pytest


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"

def test_exceptions():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:00 to 17:00")
    with pytest.raises(ValueError):
        convert("13 AM to 25 PM")