#!python
"""Software and functions to convert from arbitrary strings to
various representations of the individual characters"""
import colored


#Definition of Hex transcode function
def asHex(data):
    """String to printable hex conversion

    Creates and returns a string containing the hexadecimal
    representation of the input string.  For example, with the input
    "ABC", the function will return "0x41 0x42 0x43".

    Args:
        data (string): a string to convert into the hex representation

    Returns:
        string: a string containing the hex representation of the input

    """
    
    #Start with an empty list
    output=[]

    #Now for each character...
    for c in data:
        #Add the hex representation of the character to the string element of the list
        #The ord function returns the ASCII value of a character
        #The hex function returns the hexadecimal representation of a number
        output.append(hex(ord(c)))
        

    return output #Return of the results

    


#Definition of octal transcode function
def asOctal(data):
    """String to printable octal conversion

    Creates and returns a string containing the octal
    representation of the input string.  For example, with the input
    "ABC", the function will return "0o101 0o102 0o103".

    Args:
        data (string): a string to convert into the octal representation

    Returns:
        string: a string containing the octal representation of the input

    """
    
    #Start with an empty string
    output=[]

    for c in data:
        #Add the oct representation of the character to the string
        #The ord function returns the ASCII value of a character
        #The oct function returns the octal representation of a number
        output.append(oct(ord(c)))

    return output#.strip() #Take off any spare spaces at the start/end


#Definition of binary transcode function
def asBinary(data):
    """String to printable binary conversion

    Creates and returns a string containing the binary representation of the input string.  For example, with the input "ABC", the function will return "0b1000001 0b1000010 0b1000011"

    Args:
        data (string): a string to convert into the binary representation

    Returns:
        List of strings: a string containing the binary representation of the input

    """
    
    #Start with an empty list
    output=[]
    
    for c in data:
        #Add the bin representation of the character to the string
        #The ord function returns the ASCII value of a character
        #The bin function returns the binary representation of a number
        output.append(bin(ord(c)))

    return output #Return of the result



#Definition of ASCII transcode function
def asASCII(data):
    """String to printable ASCII conversion

    Creates and returns a string containing the ASCII
    representation of the input string.  For example, with the input
    "ABC", the function will return "65 66 67".

    Args:
        data (string): a string to convert into the ASCII representation

    Returns:
        string: a string containing the ASCII number of the input

    """
    
    #Start with an empty string
    output=[]

    for c in data:
        #Add the ASCII representation of the character to the string
        #The ord function returns the ASCII value of a character
        #The ascii function returns the ASCII number of the input
       output.append(ascii(ord(c)))

    return output #Return of result



#Definition of print function
def outPrt(transcodeName, prnInf):
    #The name of the transcoder
    print(colourise(transcodeName, "#0000FF"))
    
    i=0      #Line index
    count=0  #Counter for the number of printed strings per line
    
    print(f"0x{i}", end="") #Line number print
    
    for x in range(len(prnInf)):
        #Reserving 15 spaces for every string and printing it
        print('%15s' % prnInf[x], end="")
        if count==7:
            #New line per every 7 strings
            i+=1
            print(end='\n')
            print(f"0x{i}", end="")
            count=0
            
        else:
            count+=1
    
    print(end='\n')



#Definition of the "text color" function
def colourise(text, colour):
    return colored.fg(colour)+text+colored.attr('reset')

#Definition of the "main" function
def main():
    """This function is called when this file is executed as a
program. Usually we don't bother putting a docstring in this function,
but I decided to add this one as a simple example. 

Notice that the String is 'triple quoted'. Usually, a String in Python
is bounded by one single or double quote mark. 'Like this' "or like
this". You can also use triples like this one does. It has a few
benefits that sometimes come in handy. In particular, you can easily
include single and double quote characters within it, because it takes
three in a row to signal the end. You can also go across multiple
lines, like I have here.

    """
    
    #+++++++++++++ \/ User input part \/ +++++++++++++
    
    print(colourise("Transcoder V1.0 alpha","#7CFC00"))
    print('')
    inputData=input("Enter the data you want to transcode:")
    print(f"Input: {inputData}")
    print('')
    
    #+++++++++++++ \/ Calling of the functions \/ +++++++++++++
    
    asciiData=asASCII(inputData)
    hexData=asHex(inputData)
    octData=asOctal(inputData)
    binData=asBinary(inputData)
    
    #+++++++++++++ \/ print of the result \/ +++++++++++++
        
    outPrt('Hex', hexData)
    outPrt('Octal', octData)
    outPrt('Binary', binData)
    outPrt('ASCII', asciiData)
    
    

#Calling the "main" function
if __name__=="__main__":
    main()



# JS: You can ignore the stuff below. It's just for my spell-checker.
#  LocalWords:  Transcoder pre asHex JS inputData hexData  asOctal
#  LocalWords:  octData binData asBinary oct ord
