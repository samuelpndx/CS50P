from twttr import shorten

def test_lower():
    assert shorten("hello world") == "hll wrld"

def test_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_number():
    assert shorten("H3llo W0rld") == "H3ll W0rld"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"