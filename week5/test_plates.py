from plates import is_valid

def test_valid():
    assert is_valid("AN12") == True
    assert is_valid("CS") == True
    assert is_valid("CS#50") == False
    assert is_valid("50CS") == False
    assert is_valid("CS50A") == False
    assert is_valid("CS05") == False
    assert is_valid("CSPY") == True