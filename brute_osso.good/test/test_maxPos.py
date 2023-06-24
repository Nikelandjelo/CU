import pytest
import sys
sys.path.append("./src/")
from brute_advanced import maxPos
from brute_advanced import ASCII


def test_maxPos():
    assert maxPos([1,2,3])==2
    assert maxPos([1])==0
    assert maxPos([1,-10])==0

def test_ASCII():
    assert 'a' and 'z' and 'A' and 'Z' and '0' and '9' in ASCII()