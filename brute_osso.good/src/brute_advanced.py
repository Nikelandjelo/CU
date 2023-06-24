#!python3
import colored
from colored import stylize
from brutus import Binary


def maxPos(seq):
    """ Given a list of numbers, return the **position** of the largest
    Args:
       seq: the list to be searched
    Returns:
       an integer position of the largest number in `seq`
    """
    maxNum=seq[0]
    maxPos=0

    for i in range(len(seq)):
        if seq[i]>maxNum:
            maxNum=seq[i]
            maxPos=i

    return maxPos


def averageTry(target, promptText, failText, guess, repeats=3):
    """Function for calculating the average time for attempt with each guess
    Args:
        target: path to the binary. e.g. "./bins/basic1
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
        guess: the password guess
        repeats: for how many times we will calculate the average value
    Returns:
        a tuple containing False for incorrect password
        or True for correct one, and the average time
        for attempting"""

    results=[]
    attmpResult=[]
    success=False
    
    for i in range(repeats):
        #Attempt
        b=Binary(target)
        b.run()
        result=b.timedAttempt(promptText,guess, failText)

        attmpResult.append(result[0])
        results.append(result[1])

    success=attmpResult[0] and attmpResult[1] and attmpResult[2]
    return (success,sum(results)/len(results))


def ASCII():
    """This function generates the charactars from ASCII
    Every character from 'a' to 'z'
    Every charackter from 'A' to 'Z'
    Every charackter from '0' to '9'"""

    chars=[]

    #---a to z---
    for i in range(97, 123):
        chars+=chr(i)

    #---A to Z---
    for i in range(65, 91):
        chars+=chr(i)

    #---0 to 9---
    for i in range(48,58):
        chars+=chr(i)

    #ALL
    #for i in range(32, 127):
    #    char+=chr(i)

    return chars


def breakBinary_v2(target, promptText, failText):
    """ Break into the given target binary.
    Assumes "intermeduate level binary, with dictionary words
    Args:
        target: path to the binary. e.g. "./bins/basic1"
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
    Returns:
        None: if no successful attempt was made
        passwd+guess: a successful password"""
    
   
    asciiChars=ASCII()
    passwd=''

    while True:

        allTimeResults=[]

        for guess in asciiChars:
            #The actual attempt
            success=averageTry(target,promptText,failText,passwd+guess)

            if success[0] is True:
                print(stylize(f"\nThe Guess '{passwd+guess}' appears to be correct\n", colored.fg("green") + colored.attr("underlined")))
                return passwd+guess #Return the answer. No need to "break" because the return exits the function

            else:
                print(stylize(f"Guess: {passwd+guess} - Password incorrect!", colored.fg("red")))

            allTimeResults+=str(success[1]).split(' ')
        
        passwd+=asciiChars[maxPos(allTimeResults)]

        #Check for too long password
        if len(passwd) in [8,16,32]:
            while True:
                print(stylize("\nThe password is too big or the timing attack is not a reliable method!\n", colored.fg("red")))
                answ='N'
                answ=input("Continue?(y/N): ")

                if answ.upper().strip() in ['N','NO']: return None
                elif answ.upper().strip() in ['Y','YES']:
                    print('\n')
                    break
                else: print('\nIncorrect input!\n')


if __name__=="__main__":

    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["targets/advanced1","Password:", "Password Incorrect"])
    targets.append(["targets/advanced2","Password:", "Password Incorrect"])
    targets.append(["targets/advanced3","Password:", "Password Incorrect"])

    print(stylize("Advanced Binary Breaker\n", colored.fg("blue") + colored.attr("bold")))
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
        print(stylize(f"{c}: {targets[c][0]}", colored.fg("green")))

    selection=int(input("Enter the number of the binary to be forced: "))
    print('\n')

    if 0 <= selection < len(targets):
        target=targets[selection]
        breakBinary_v2(target[0],target[1],target[2])
    else:
        print(stylize("Invalid selection", colored.fg("red")))