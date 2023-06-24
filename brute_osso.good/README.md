# :tomato:Osso Good:bell:

## Table of contents

   * [:one: Introduction:](#introduction)
   * [:two: User documentation:](#user-documentation)
      * [:hash:1 Files support and usage](#1-files-support-and-usage)
      * [:hash:2 Passwords](#2-passwords)
      * [:hash:3 Setup](#3-setup)
      * [:hash:4 Usage](#4-usage)
   * [:three: Unit Tests:](#unit-tests)
   * [:four: Algorithms:](#algorithms)
      * [:hash:1 Creating a list of all possible three-digit PINs](#creating-a-list-of-all-possible-three-digit-pins-)
      * [:hash:2 Creating a list of password attempts by modifying dictionary words](#creating-a-list-of-password-attempts-by-modifying-dictionary-words-)
      * [:hash:3 Cracking a password using a timing attach](#creating-a-list-of-password-attempts-by-modifying-dictionary-words-)


## Introduction:

The purpose of this project is to break through binaries password using the brute-force method. The brute-force method is breaking password by trying guessing every possible combination for this specific password. For example, if the password can be any combination of the digits from 0 to 9 with a length of three symbols we can try to "brute-force it" by trying every combination. And this is exactly the first functionality of the project."brute_basic.py" can break every password into the radius of “000” to “999”. But this is not the only feature of this project. There are three versions of it.

**"brute_basic.py"** - Trying to crack passwords by generating every possible combination of symbols using the digits from 0 to 9 with a length of the combinations three. This is the fastest version but in real-live can be used only for PIN braking.

**"brute_intermediate.py"** - Unlikely "brute_basic.py", "brute_intermediate.py" is more reliable to the real-life. The script is using the "dictionary" method furthermore generates permutations for every word into this word list.

**"brute_advanced.py"** - The third version is based on timing attacks. The script tries to break the password with every symbol as well as detects the time required for responding. The symbol which requires the longest time is being added to the password string. After that starts trying the next symbol and so on.


## User documentation:

### 1. Files support and usage  
   All of the versions support the binary file format and scripts. The ones the scripts are tested with are in /targets directory. The way to add your own binary is with adding the highlighted line into any of the scripts you want to use:

   ```python3
   #Create a simple menu system to pick the binary we want to force
   targets=[]
   targets.append(["targets/basic1","Password:", "Password Incorrect"])
   targets.append(["targets/basic2","Enter the secret code:", "ACCESS DENIED"])
   targets.append(["targets/basic3","Got the PIN?", "NO"])
   targets.append(["PATH_TO_TARGET","OUTPUT_BEFORE_PASSWORD","OUTPUT_AFTER_INCORRECT_PASSWORD"]) 
   ```
   - On the place of "PATH_TO_TARGET" put the path to your binary.
   - On the place of "OUTPUT_BEFORE_PASSWORD" put the text printed before the password input.
   - On the place of "OUTPUT_AFTER_INCORRECT_PASSWORD" put the text printed after entering wrong password.

### 2. Passwords  
   Every version of the project supports different types of passwords.

   **brute_basic.py:** [![src/brute_basic.py](https://img.shields.io/badge/src-brute__basic.py-blue)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_basic.py)  
   It supports PINs with a length of three digits from 0 to 9.
   Basically, PINs into the range of "000" to "999".

   **brute_intermediate.py:** [![src/brute_intermediate.py](https://img.shields.io/badge/src-brute__intermediate.py-yellow)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_intermediate.py)  
   It supports dictionary passwords with any length and symbols. Furthermore, it creates a max of 11 permutations of any word. First, the script generates versions of every word into the word list plus the digits from 0 to 9.  

   If you want to use your word list or to include one to the default one you can:
   - To add another word list, add the highlighted line:

   ```python3
   #Load the dictionary
   words=wordsFromFile("dictionaries/base.txt")
   words.append(wordsFromFile("PATH_TO_FILE/NAME_OF_FILE"))
   words+=permutation(words)
   ```

   On the place of **"PATH_TO_FILE"** put the path to your word list.
      E.g.: home/user/../

   On the place of  **"NAME_OF_FILE"** put your word list file name.
         E.g.: wordlist.txt

   - To use only yours word list, edit this line by adding the path to the file and the name:

      ```python3
      #Load the dictionary
      words=wordsFromFile("dictionaries/base.txt")
      words+=permutation(words)
      ```

   **brute_advanced.py:** [![src/brute_advanced.py](https://img.shields.io/badge/src-brute__advanced.py-red)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_advanced.py)  
   The advanced version of the project can generate every possible password which includes the digits from 0 to 9, the lower letters from "a" to "z", and the upper ones from "A" to "Z".

### 3. Setup  
   Requirements for installing:  
   - Linux or BSD OS (Tested on Arch and Kali Linux)
   - python3
   -  pip3
   - git (optional)  
  
   Installing:

   1. Download the zip or clone the repository if using git
   ```shell
   git clone https://github.coventry.ac.uk/ivanovn/brute_osso.good.git
   ```
   2. Extract (if used zip) change the directory in the repository folder, activate venv and install the libs
   ```shell
   cd brute_osso.good
   make venv
   . ./brute_venv/bin/activate
   make prereqs
   ```
   3. Run  
   Into the repository directory **/brute_osso.good** write one of the following lines:
   ```shell
   src/[version_of_the_script]
   or
   ./src/[version_of_the_script]
   or
   python3 src/[version_of_the_script]
   ```
   Replace **[version_of_the_script]** with **brute_basic.py**, **brute_intermediate.py** or **brute_advanced.py**

### 4. Usage  
   After we run any of the scripts, we can see the simplistic interface:  
   ![](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/Photos/1.png?raw=true)

   The testing targets can be downloaded by running the download_targets.sh script:
   ```shell
   ./download_targets.sh
   ```

   After starting the app, we can choose which target's password we want to crack, and then the script is going to start its work:  

   ![](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/Photos/2.png?raw=true)


   If the password is found, the script will print it out:  

   ![](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/Photos/3.png?raw=true)

## Unit Tests:

   |Function|Test|Expected result|
   |---|---|---|
   |guessGenerator()|Generation of ‘000’|'000'|
   |guessGenerator()|Generation of ‘999’|'999'|
   |guessGenerator()|Length of  every PIN|3|
   |guessGenerator()|Length of return|1000|
   |permutation()   |Comparing permutations with  strings prepared strings|'000', '111', '444', '555',  '333', '01453', '35410',  '014', '410', '140', '041',  '104', '401', 'ooo0', 'ooo9',  'aoi5'|
   |ASCII()         |Generation of 'a', 'z',  'A', 'Z', '0' and '9'|'a', 'z', 'A',  'Z', '0', '9'|

## Algorithms:
### Creating a list of all possible three-digit PINs [![src/brute_basic.py](https://img.shields.io/badge/src-brute__basic.py-blue)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_basic.py)
   The algorithm used for this script generates every number from 0 to 999 and checks the length of the number. If the number is with a length of 2 digits, adds one 0 in front. If the number is with a length of 1 digit, adds two 0 in front.
   Originally, I was going to use an algorithm, which generates digits from 0 to 9 for every digit from 0 to 9, which are generated for every number from 0 to 9. AKA nasty for loop.
   ```python3
   for num0 in range(10):
	   for num1 in range(10):
		   for num2 in range(10):
   ```
   In fact, I would choose this method in every other language but, since python is famous for its slow for loop, I preferred the if statements.

### Creating a list of password attempts by modifying dictionary words [![src/brute_intermediate.py](https://img.shields.io/badge/src-brute__intermediate.py-yellow)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_intermediate.py)
   This script uses algorithm which for every string in list of strings add the digits from 0 to 9 and append the result in new list. After that checks the original strings if they contain the characters 'o', 'i', 'e', 'a' and 's' replacing them accordingly with '0', '1', '3', '4' and '5', and again append the new strings in list. After that returns the new list.

### Cracking a password using a timing attach [![src/brute_advanced.py](https://img.shields.io/badge/src-brute__advanced.py-red)](https://github.coventry.ac.uk/ivanovn/brute_osso.good/blob/master/src/brute_advanced.py)
   This script uses a timing attack algorithm. It tries as password every ASCII character from 'a' to 'z', 'A' to 'Z' and '0' to '9' three times. After that, calculate the average time between these three attempts. If non of the characters is the correct password the one with higher time for attempting is added to a string used as password guess. The loop is repeating, but this time the current symbol is appended to this string, containing the previous character. Again, added to the password guess is the one with the highest time for attempting. The loop is working until a successful attempt or has stopped from the operator.

**P.S. Just noticed, that every commit from the command line, has been done from my personal git. If it's needed, I can provide evidence for the account. This will be prevented in the future. Thanks.**
