
"""
Write a Python script that prompts the user for a number and displays a message 
to indicate if the number is odd or even.

Note: do consider 0 has being neither odd nor even.

To retrieve the number you should use input()
Dont forget to convert the value returned by input into an int 
with the help of int()
Then use the Modulo (%) operator to test if the number given is odd or even

"""

aNumber=input("Please enter an integer: ")

aNumber=int(aNumber)

if aNumber == 0:
    print("The number entered", aNumber, "is zero")
elif aNumber % 2 == 0:
    print("The number entered", aNumber, "is even")
elif aNumber % 2 == 1:
#else:
    print("The number entered", aNumber, "is odd")    