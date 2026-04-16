import pytest
from response import validate

def test_valid():
    assert validate("malan@harvard.edu") == True
    assert validate("user.name+tag@example.co.uk") == True

def test_invalid():
    assert validate("not-an-email") == False
    assert validate("@nodomain.com") == False
    assert validate("noatsign.com") == False
    assert validate("missing@tld") == False
