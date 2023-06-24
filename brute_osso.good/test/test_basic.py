import pytest
import sys
sys.path.append("./src/")
from brute_basic import generateGuesses_v1 #Change to "..._v1" if testing the second version


def test_guessGenerator():
    #Test for furst posible PIN
    assert '000' in generateGuesses_v1()
    
    #Test fo last posible PIN
    assert '999' in generateGuesses_v1()

    #Test if every guested PIN has lengh of tree simbols
    for i in generateGuesses_v1():
        assert len(i)==3

    #Test if the lengh of the list is 1000 (1000 posible PINs)
    assert len(generateGuesses_v1())==1000