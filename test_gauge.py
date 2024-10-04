import pytest
from gauge_v2 import convert, gauge


def test_x_greater():
    with pytest.raises(ValueError):
        convert("8/7")


def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("0/1") == 0


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
