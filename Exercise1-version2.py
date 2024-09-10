
"""
Write a Python script that prompts the user for a number and displays a message 
to indicate if the number is odd or even.

Note: do consider 0 has being neither odd nor even.

To retrieve the number you should use input()
Dont forget to convert the value returned by input into an int 
with the help of int()
Then use the Modulo (%) operator to test if the number given is odd or even

After having tested a first number, the script should prompt the user for other numbers as long as he or she would like to.

You can use a while loop with a loop condition based on the answer of the user
to the question: "Do you want to do another test ?"

"""

while True:
    
    aNumber=input("Please enter an integer: ")
    
    aNumber=int(aNumber)
    
    if aNumber == 0:
        print("The number entered", aNumber, "is zero")
    elif aNumber % 2 == 0:
        print("The number entered", aNumber, "is even")
    else:
        print("The number entered", aNumber, "is odd")    
        
    response=input("Do you want to do another test ('yes' or 'no')? ")
    
    if response != "yes": # of if response == "no":
        break