import pytest
from um import count

def test_single():
    assert count("Um, hello") == 1
    assert count("um") == 1

def test_multiple():
    assert count("Um, um, um") == 3

def test_case_insensitive():
    assert count("UM um Um") == 3

def test_not_substring():
    assert count("umbrella") == 0
    assert count("yummy") == 0
    assert count("album") == 0

def test_zero():
    assert count("hello world") == 0
