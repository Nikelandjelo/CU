#!python3
import colored
from colored import stylize
from brutus import Binary
#import time


def generateGuesses_v1():
    """Generate guesses for PINs with lengh of three numbers from '0' to '9'"""
    """                         from '000' to '999'                         """

    singlePIN=""
    guess=[]
    #timeForGen1=time.perf_counter()#Time1

    #Generate every guess from '000' to '999'
    for num in range(1000):
        if len(str(num))==3: singlePIN=str(num)
        elif len(str(num))==2: singlePIN=("0"+str(num))#Adding '0' infront of the numbers from 10 to 99
        elif len(str(num))==1: singlePIN=("00"+str(num))#Adding '00' infront of the numbers from 0 to 9

        guess.append(singlePIN)

    #timeForGen2=time.perf_counter()#Time2
    #print(f'\nGenerated for: {timeForGen2-timeForGen1}')
    return guess


#def generateGuesses_v2():
    #"""Generate guesses for PINs with lengh of tree numbers from '0' to '9'"""
    #"""                         from '000' to '999'                        """
    #
    #singlePIN=""
    #guess=[]
    #timeForGen1=time.perf_counter()#Time1
    #
    ##Generate every guess from '000' to '999'
    #for num0 in range(10):
    #    for num1 in range(10):
    #        for num2 in range(10):
    #            singlePIN=str(num0)+str(num1)+str(num2)
    #            guess.append(singlePIN)
    #
    #timeForGen2=time.perf_counter()#Time2
    #print(f'\nGenerated for: {timeForGen2-timeForGen1}')
    #return guess


def breakBinary(target, promptText, failText):
    """" Break into the given target binary.
    Assumes "basic" level binary, with PIN codes of 000-999
    Args:
        target: path to the binary. e.g. "./bins/basic1"
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
    Returns:
        None: if no successful attempt was made
        string: a successful password"""


    guesses=generateGuesses_v1()
    
    for guess in guesses:        

        #The actual attempt
        b=Binary(target)
        b.run()
        success=b.attempt(promptText, guess, failText)

        
        if success:
            print(stylize(f"\nThe Guess '{guess}' appears to be correct\n", colored.fg("green") + colored.attr("underlined")))
            return guess #Return the answer. No need to "break" because the return exits the function
        else:
            print(stylize(f"Guess: {guess} - Password incorrect!", colored.fg("red")))
    return None #If we get here, it means we didn't return earlier in the loop with a successful guess

    
if __name__=="__main__":


    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["targets/basic1","Password:", "Password Incorrect"])
    targets.append(["targets/basic2","Enter the secret code:", "ACCESS DENIED"])
    targets.append(["targets/basic3","Got the PIN?", "NO"])


    print(stylize("Basic Binary Breaker\n", colored.fg("blue") + colored.attr("bold")))
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
        print(stylize(f"{c}: {targets[c][0]}", colored.fg("green")))

    selection=int(input("Enter the number of the binary to be forced: "))
    print('\n')

    if 0 <= selection < len(targets):
        target=targets[selection]
        breakBinary(target[0],target[1],target[2])
    else:
        print(stylize("Invalid selection", colored.fg("red")))
