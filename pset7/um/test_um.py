from um import count

def test_count():
    assert count("Um") == 1
    assert count("um") == 1
    assert count("Hello, um, hum!") == 1