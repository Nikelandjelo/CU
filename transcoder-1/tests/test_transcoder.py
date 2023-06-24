import pytest
import sys
sys.path.append("./src/")
import transcoder


    





def test_asHex():
    """ Test the 'asHex' function """

    #First a simple string
    testABC=['0x41', '0x42', '0x43']
    assert transcoder.asHex("ABC")==testABC or "'0x41' '0x42' '0x43'"
    #An empty string
    testEmpty=[]
    assert transcoder.asHex("")==testEmpty or ""
    #The highest byte value
    test255=["0xff"]
    assert transcoder.asHex(chr(255))==test255 or "0xff"
    #Lowest byte value
    test0=['0x0']
    assert transcoder.asHex(chr(0))==test0 or "0x0"
    



def test_asOctal():
    """ Test the 'asOctal' function """

    #First a simple string
    testABC=['0o101', '0o102', '0o103']
    assert transcoder.asOctal("ABC")== testABC or "'0o101' '0o102' '0o103'"
    #An empty string
    testEmpty=[]
    assert transcoder.asOctal("")==testEmpty or ""
    #The highest byte value
    test255=['0o377']
    assert transcoder.asOctal(chr(255))==test255 or "0o377"
    #Lowest byte value
    test0=['0o0']
    assert transcoder.asOctal(chr(0))==test0 or "0o0"
    
    
def test_asBinary():
    """ Test the 'asBinary' function """

    #First a simple string
    testABC=['0b1000001', '0b1000010', '0b1000011']
    assert transcoder.asBinary("ABC")==testABC or "0b1000001 0b1000010 0b1000011"
    #An empty string
    testEmpty = []
    assert transcoder.asBinary("")==testEmpty or ""
    #The highest byte value
    test255=['0b11111111']
    assert transcoder.asBinary(chr(255))==test255 or "0b11111111"
    #Lowest byte value
    test0=['0b0']
    assert transcoder.asBinary(chr(0))==test0 or "0b0"



def test_asASCII():
    """ Test the 'asASCII' function """

    #First a simple string
    testABC=['65', '66', '67']
    assert transcoder.asASCII("ABC")==testABC or "65 66 67"
    #An empty string
    testEmpty=[]
    assert transcoder.asASCII("")==testEmpty or ""
    #The highest byte value
    test255=['255']
    assert transcoder.asASCII(chr(255))==test255 or "255"
    #Lowest byte value
    test0=['0']
    assert transcoder.asASCII(chr(0))==test0 or "0"
