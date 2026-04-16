from plates import is_valid


def test_valid():
    assert is_valid("AA") == True
    assert is_valid("AAA123") == True
    assert is_valid("CS50") == True


def test_too_short_or_long():
    assert is_valid("A") == False       # trop court
    assert is_valid("AAAAAAA") == False # trop long (7 chars)


def test_must_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False      # only 1 letter before digit


def test_no_zero_as_first_digit():
    assert is_valid("CS05") == False
    assert is_valid("AA01") == False


def test_no_letters_after_digits():
    assert is_valid("AA1B") == False
    assert is_valid("CS50P") == False


def test_no_punctuation_or_spaces():
    assert is_valid("AA !") == False
    assert is_valid("AA.BB") == False
