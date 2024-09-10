
"""

while condition:
    statement 1
    statement 2

statement 3

The statement break can be used to leave a while loop irrespective of the
value of the loop condition

"""


nb=5

while True:
    print("In the loop: nb is", nb)
    nb = nb - 1
    if nb == 0:
        break

print("End of the script")
    
    
