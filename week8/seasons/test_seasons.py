from seasons import get_birth
import pytest

def test_valid():
    assert get_birth("2002-04-04") == (2002, 4, 4)

def test_invalid_format():
    with pytest.raises(SystemExit):
        get_birth("April 4, 2002")

def test_invalid_date():
    with pytest.raises(SystemExit):
        get_birth("9999-99-99")
