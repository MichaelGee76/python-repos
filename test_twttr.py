import pytest
from twttr import shorten


# test single words
def test_single():
    assert shorten("fish") == "fsh"
    assert shorten("frog") == "frg"
    assert shorten("abracadabra") == "brcdbr"


# test multiple words
def test_multiple():
    assert shorten("The fish does not smell so badly") == "Th fsh ds nt smll s bdly"
    assert shorten("No way that you have been doing that") == "N wy tht y hv bn dng tht"


# test lower case word/words
def test_lower():
    assert shorten("wague steak is the best") == "wg stk s th bst"
    assert shorten("filet") == "flt"


# test upper case word/words
def test_upper():
    assert shorten("MY CHICKS ARE MY BESTIES") == "MY CHCKS R MY BSTS"
    assert shorten("DO NOT EAT YELLOW SNOW") == "D NT T YLLW SNW"
    assert shorten("BOOMBOOMBOOM") == "BMBMBM"
