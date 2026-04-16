import pytest
from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("256.256.256.256") == False
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.1000") == False
