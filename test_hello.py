from hello_hello import hello


def test_argument():
    assert hello("David") == "hello, David"


def test_no_argument():
    assert hello() == "hello, world"
