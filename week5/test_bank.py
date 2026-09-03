from bank import value

def test_value():
    assert value("hello there") == "$0"
    assert value("HELLO THERE") == "$0"
    assert value("h") == "$20"
    assert value("Good morning") == "$100"
    assert value("Thank you") == "$100"
