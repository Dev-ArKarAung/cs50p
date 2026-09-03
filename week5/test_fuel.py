from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50.0
    assert convert("3/4") == 75.0
    assert convert("1/4") == 25.0

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("5/2")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"