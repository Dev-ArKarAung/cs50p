from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"

def test_shorten_lowercase():
    assert shorten("xyz") == "xyz"