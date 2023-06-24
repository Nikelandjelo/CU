import pytest
import sys
sys.path.append("./src/")
from brute_intermediate import permutation

def test_permutation():

    test=['ooo', 'iii', 'aaa', 
    'sss', 'eee', 'oiase', 
    'esaio', 'oia', 'aio',
    'iao', 'oai', 'ioa', 'aoi']

    permutatedTest=['000', '111', '444', 
    '555', '333', '01453', 
    '35410', '014', '410', 
    '140', '041', '104', 
    '401', 'ooo0', 'ooo9', 'aoi5']

    #Testing if the syimbols are replaced right and if the nums from 0 to 9 are added
    for i in permutatedTest: assert i in permutation(test)