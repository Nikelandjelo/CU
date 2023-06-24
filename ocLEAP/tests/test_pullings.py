#! /usr/bin/env python
import pytest
import sys
sys.path.append("./src/")
from kmPullings import Enum1
from kmPullings import Enum2
from kmprivage import Shadow

def test_pullings():
    assert Enum1() != Enum2()                   
def test_privage():
    pass