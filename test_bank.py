import pytest
from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("h") == 20


def test_not_h():
    assert value("Friend") == 100


def test_upper():
    assert value("HELLO") == 0


def test_phrase():
    assert value("Under water there is nothing") == 100
    assert value("Hello my name is Paul") == 0
    assert value("Have a good night") == 20
