"""

Write a Python scripts that implements the “Guess the Number” game.
The script will generate of a random integral number (use the module random) 
from 1 to 100, and ask you to guess it.
The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.

"""

import random # this is to have access to the function that generate random int

# Step 1: generate a random int in the range [1,100]
# Step 2: prompt the user for up to 6 values (with the help of a while loop)
# Step 2.1: each time a new value is given, compare it with the random int
# and display the proper message "Too large", "Too small", "Bingo !"
# Step 2.2: as soon as the secret number is found leave the script
# Step 2.3: as soon as a maximum number of attempts (6) to guess the secret 
# number is reached, leave the script

# to generate a "pseudo" random int in the range [1,100]
secret=random.randint(1,100)

print(secret) # This to help testing my script :-) !

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:

    currentValue=input("Enter an int in the range [1,100]: ")
    
    currentValue=int(currentValue)

    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break # to leave the loop immediately 
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small !") 
        
    currentNumberOfAttempts = currentNumberOfAttempts + 1
    
# If I reach this point, it means the while loop is terminated but why ?
# Because of the use of break (in this case there is nothing to do)? 
# Because a the loop condition (in this case I print the secret number)?
   
if secret != currentValue:
    print("The secret number was:", secret)