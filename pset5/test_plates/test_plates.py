from plates import is_valid

def test_valid_size():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CSCSCSC") == False


def test_only_letters_and_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS-50") == False
    assert is_valid("PI3.14") == False
    assert is_valid("3.14") == False


def test_start_two_letters():
    assert is_valid("CSCS") == True
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("50CS") == False
    assert is_valid("..CS50") == False
    assert is_valid("5") == False


def test_number_in_middle():
    assert is_valid("CS50CS") == False
    assert is_valid("CS050") == False
    assert is_valid("SA32") == True