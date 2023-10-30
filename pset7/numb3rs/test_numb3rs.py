from numb3rs import validate

def test_names():
    assert validate("cat") == False
    assert validate("dog") == False

def test_ip_valid():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("249.249.249.249") == True
    assert validate("100.100.100.100") == True
    assert validate("255.1.1.1") == True
    assert validate("255.0.0.0") == True
    assert validate("1.255.1.1") == True

def test_ip_invalid():
    assert validate("1000.1.1.1") == False
    assert validate("1.1000.1.1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("256.1.1.1") == False
    assert validate("255.cat.1.1") == False
    assert validate("cat.255.255.255") == False
    assert validate("255...") == False
    assert validate("255") == False
    assert validate("255.256.255.256") == False

