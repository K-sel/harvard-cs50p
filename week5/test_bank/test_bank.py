from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, how are you?") == 0
    assert value("HELLO!") == 0


def test_h():
    assert value("How are you?") == 20
    assert value("Howdy") == 20
    assert value("hi there") == 20


def test_other():
    assert value("What's up?") == 100
    assert value("Sup") == 100
    assert value("Good morning") == 100
