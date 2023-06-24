#!python3
import colored
from colored import stylize
from brutus import Binary


def wordsFromFile(filePath):
    """ Read lines from a file containing one word per line and return a list of the words
    Args:
        filePath: the absolute or relative path of the file to be read
    Returns:
        a list of the words from the file, stripped of whitespace
    """
    f=open(filePath,"r")
    out=[]
    for l in f.readlines():
        w=l.strip()
        if len(w)>0:
            out.append(w.lower())
    f.close()
    return out


def breakBinary(target, promptText, failText, guesses):
    """ Break into the given target binary.
    Assumes "intermeduate level binary, with dictionary words
    Args:
        target: path to the binary. e.g. "./bins/basic1"
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
        guesses: list of words to try as passwords
    Returns:
        None: if no successful attempt was made
        string: a successful password""" 
    
    for guess in guesses:        

        #The actual attempt
        b=Binary(target)
        b.run()
        success=b.attempt(promptText,guess, failText)

        
        if success:
            print(stylize(f"\nThe Guess '{guess}' appears to be correct\n", colored.fg("green") + colored.attr("underlined")))
            return guess #Return the answer. No need to "break" because the return exits the function
        else:
            print(stylize(f"Guess: {guess} - Password incorrect!", colored.fg("red")))
    return None #If we get here, it means we didn't return earlier in the loop with a successful guess


def permutation(words):
    """This function generate permutation of list of strings
    Each word with all 0-9 digits appended (so 'swordfish' would be 'swordfish0', 'swordfish1' etc.
    Each word turned into "l33t-5p34k"
    Each o becomes 0, each i becomes 1, each a becomes 4, each s becomes 5, each e becomes 3
    'swordfish' becomes '5w0rdf15h', for example
    Args:
        words: list of strings (words that going to be used for the permotations)
    Returns:
        perm: list of permutations of the 'words'"""

    perm=[]

    #Adding digits from '0' to '9' to each word
    for i in range(10):
        for word in words:
            word+=str(i)
            perm.append(word.strip())

    #Replacing each o with 0, each i with 1, each a with 4, each s with 5, each e with 3
    for word in words:
        if 'o' in word: word=word.replace('o', '0')
        if 'i' in word: word=word.replace('i', '1')
        if 'a' in word: word=word.replace('a', '4')
        if 's' in word: word=word.replace('s', '5')
        if 'e' in word: word=word.replace('e', '3')

        perm.append(word.strip())
        

    return perm

 
if __name__=="__main__":

    #Load the dictionary
    words=wordsFromFile("dictionaries/base.txt")
    words+=permutation(words)

    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["targets/intermediate1","Password:", "Password Incorrect"])
    targets.append(["targets/intermediate2","Secret code:", "Auth Failure"])
    targets.append(["targets/intermediate3","Enter Credentials:", "Invalid Credentials"])

    print(stylize("Intermediate Binary Breaker\n", colored.fg("blue") + colored.attr("bold")))
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
         print(stylize(f"{c}: {targets[c][0]}", colored.fg("green")))

    selection=int(input("Enter the number of the binary to be forced: "))
    print('\n')

    if 0 <= selection < len(targets):
        target=targets[selection]
        breakBinary(target[0],target[1],target[2], words)
    else:
        print(stylize("Invalid selection", colored.fg("red")))