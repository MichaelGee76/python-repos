import pytest
from calcuter import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# mit der pytest method raises teile ich mit, dass ich einen typeerror erwarte.


def test_str():
    with pytest.raises(TypeError):
        square("5")
