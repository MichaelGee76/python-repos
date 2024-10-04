import pytest
from plates import is_valid


# All vanity plates must start with at least two letters
def test_alphabetics():
    assert is_valid("CS50") == True
    assert is_valid("ABCD12") == True
    assert is_valid("55CS50") == False
    assert is_valid("C5550") == False
    assert is_valid("C") == False


# Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters
def test_length():
    assert is_valid("CS505055") == False
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("ABCD50") == True
    assert is_valid("ABCDE12") == False


# Numbers cannot be used in the middle of a plate
def test_numbers_position():
    assert is_valid("AB50CD") == False
    assert is_valid("AAA222") == True
    assert is_valid("22CSCS") == False
    assert is_valid("CSKFC1") == True
    assert is_valid("CS50A1") == False


# Cannot start with 0
def test_starts_with_zero():
    assert is_valid("00CS") == False
    assert is_valid("0ABC50") == False
    assert is_valid("CS05") == False


# No periods, spaces, or punctuation marks are allowed
def test_punctuation():
    assert is_valid("CS50!") == False
    assert is_valid("CS.50,!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50@") == False
