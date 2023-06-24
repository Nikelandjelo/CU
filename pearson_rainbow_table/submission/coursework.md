# 5062CEM Coursework 1

 - Student ID: 10223282
 - GitHub Rep: https://github.coventry.ac.uk/ivanovn/pearson_rainbow_table
 
## Task 1: Passwords and Hashes (10%)

    If the hashes produced are all 2 bytes, how many possible hash values are there? Explain how you calculate this value.
	
	
2 bytes are equal to 16 bits. Binary provides two options: 0 and 1. 2 bytes (16 bits) provides 16 positions.
2 options to the power of 16 positions give us 65,536 possible combinations.

`2^16 = 65536`


    With minimum password length of 3 and maximum of 6, and possible characters being all upper and lowecase letters and digits (ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789) how many possible passwords are in our "search space"? Explain how you calculate this value.
	
	
Following the logic from before, we have 3 to 6 possible positions. We also have 26 upper and 26 lowercase letters plus 10 digits, which gives us 62 possible options per position. So, 62 options to the power of 3, 4, 5, and 6 will give us 57,731,383,080 possible passwords.

`62^3 + 62^4 + 62^5 + 62^6 = 57731383080`


    One of these numbers is larger than the other. What implications does this have for security if this hash function is used in storing passwords?  What implications does this have for our rainbow table?

As the amount of hashes is so small, we would have a huge percentage of collisions, which means that more than one password will generate the same hash.
For example, the passwords `1234` and `4321` might give the same output. That is a big security issue as even if a password is secure enough another password that gives the same hash as output would work successfully. This also means that the brute-force attempts for cracking a password will give a higher success percentage.

Looking over the implication that this issue has over the rainbow table, this will give us a huge percentage of repeated hashes. This means that our rainbow table will lose a lot of storage over hashes that are already recorded in the table.
	
## Task 2: Implementing the table (30%)

Include your `generateTable` function below. The three back-ticks before and after the code tell Markdown that the text between should be marked-up as code.


``` python

def generateTable(chainStarts, hashFunc, guessFunc, chainLength, minLen=3,maxLen=6,charset=defaultCharset):
    """ Create a rainbow table for the given hash function. Initialising the chain, generating hashes for N(chainLength) guesses. The chain contains a key value pair between the last hash and the first guess.

    Arguments:
      chainStarts -- a list of starting values. The length of this list determines how many chains will be constructed.
      hashFunc -- a hash function to be used in the hashing step.
      guessFunc -- a function that can produce valid inputs to the hash function. The function should accept a value and the keyword arguments `minLen` (minimum guess length) `maxLen` (maximum guess length) and `charset` (a string containing all valid characters to be used in the table). These will be passed directly from the arguments of the same names given to this funciton.
      chainLength -- length of each chain
      minLen -- minimum length of values to be hashed
      maxLen -- maximum length of values to be hashed
      charset -- string containing all valid characters for values being hashed
    
    """

    #### Set a dictinary which get the last hash and the first guess as key value pairs. Plays the role of the table
    rtable = {}

    #### Generate the ranbow table
    for guess in chainStarts:
        #### Save the first guess so it can be used as a value in the dictinary
        firstGuess = guess

        #### Generate the chain
        for i in range(chainLength+1):
            #### Get a hash for a guess
            h = hashFunc(guess)
            #### Generate a new guess
            guess = guessFunc(h, i, minLen, maxLen, charset)

        #### Save a chain (key value pair of last hash and first guess) to the table / "|=" == ".update()"
        rtable |= {h: firstGuess}

    #### Return rainbow table
    return rtable

```
 
## Task 3: Parameters (10%)
 
    Discuss how to select the best parameters for generating a rainbow table.


Some hints:

  - You can change the number of chains and the length of each chain
  - What effect does changing each of these have on:
    - How well the table works, as in how many hashes it can break?
    - How long it takes to create?
	- How much space it takes up?
    - How long it takes to search the chains for hashes?


In a nutshell, the longer the chains are, the less space and the more time they will take. However, the more chains we make, the more space they will take less time to generate. This trade space for time is not just in the generation but also in querying the table. If we are trying to find a hash in a table with 200 chains with a length of 20 each, the time will be significantly less to query the whole table in comparison to a table with 20 chains with a length of 200 each.  
As a piece of evidence I will show the result of the example from above:

Table with 200 chains with a length of 20 each:  
Time to generate: 0.1467123031616211s  
Size in bits: 16384B  
Rows: 192  
Time to query the whole table: 0.014216184616088867s  

Table with 20 chains with a length of 200 each:  
Time to generate: 0.29982948303222656s  
Size in bits: 2672B  
Rows: 19  
Time to query the whole table: 3.432568311691284s  

(These tests are made before optimising the `makeGuess` function, which gives even a bigger difference in the results!)

	
## Task 4: Reversing Hashes (10%)

    What are possible passwords that produce the following hashes?

 - BA FF    -->>    uBg, oi0i
 - BE 21    -->>    05O, grO, SYN, VNB
 - 12 34    -->>    6UvNFX, C1HV, sWe
 - 9A 2E    -->>    zAZbpd
 
(Write your answers next to the hashes above. HINT: you can check your answers by putting them into the pearson hashN function and seeing if they give you the right hash)


## Task 5: Improving Guess Generation Efficiency (20%)

    The function that currently produces guesses is not as efficient as it could be.

    Discuss how the time it takes is related to the index argument and propose a solution that makes it independant of this value.


The original `makeGuess` function has a fairly inefficient part which can slow down the rainbow table generation drastically, especially if the table aim is longer chains. The part that needs optimisation is:

``` python
random.seed(value)

for x in range(i*maxLen):
        random.random()
```

The random seed is set to the value of the hash of the previous guess. However, to avoid collisions and set a status of the random generator which will give us a random value, the algorithm is going through "for" loop, which loops for the range from 0 to i (index indicating our position in the chain) multiplied by maxLen (maximum length of the guess, which is 6).

It is fairly obvious to spot how to avoid slowing down the algorithm. If we set a seed that is unique, the loop will not be needed anymore as the status of the random generator will be in a completely independent position from the previous guess. However, we need to make sure that we can still have access to the seeds as they are required for the rebuilding. This means that we cannot use `random.seed(random.random())` as a seed. However, we could just combine the string of the hash and the index into one value. This value is independent of the previous guess, so our next guess won't have similarities unless a random similarity appears.

Test over a table with 200 chains with a length of 200 each:

Original function:  
Time to generate: 6.487232446670532s  
Time to query the whole table: 8.330552339553833s

New function:  
Time to generate: 5.2890565395355225s  
Time to query the whole table: 7.436275005340576s

(For testing if the build chain function is working as expected, the hash "BE21" can be used. Should be found in the chain beginning with "g3T5Le" on position 95 on table 200x200)

``` python

def makeGuess(value, i, minLen,maxLen,charset, debug=False):
    """ Given a value and an index, return a new valid input.

    Arguments:
      value -- a hash value to be turned into a new guess
      i -- the number of steps along the chain we are
      minLen -- minimum length of a new guess
      maxLen -- maximum length of a new guess
      charset -- string containing the valid characters for a guess
      debug -- set to True for copious output, useful for debugging
    """
    
    #Use string of value and i as seed
    random.seed(str(value)+str(i))

    #Determine a length of the guess
    l=random.randint(minLen,maxLen)
    guess="".join(random.choices(charset, k=l))
    
    if debug: print(f"Making guess from [{value}], with offset {i}, minLen {minLen}, maxLen {maxLen} and charset {charset}: {guess}")

    return guess

```

## Challenge: Web service compromise (20%)

The docker container `cueh/pears_tree:latest` uses unsalted 2-byte pearson hashes for checking passwords.  See if you can steal the password list and find passwords that result in the hashes.

To run the container: `docker run -it cueh/pears_tree:latest`. The container should tell you which IP and port to use. If it's the only running container, it will probably be: `http://172.17.0.2:80`.

If you're doing it on a chromebook, use this instead: `docker run -p 8000:80 -it cueh/pears_tree:latest` and browse to `http://penguin.linux.test:8000`

You should submit the usernames you found, along with matching
passwords that will work on the site.

    Write a short description of how you found the hashes and used them to gain access to the site.
	
	List the hashes you found and passwords that can be used for the found usernames.

The web application is vulnerable to directory listing. After enumerating and fuzing the site, I was able to find the `/static` directory with the `dirb` tool by running `dirb http://172.17.0.2`. After visiting the path, I found the password listed there.

Path to password file: `http://172.17.0.2/static/password`

- root: 5B 1B     -->>    vLC3
- sally: FF 4A    -->>    e2gn97, z4Q
- duncan: 50 CB   -->>    x8q, KjQ3bU
