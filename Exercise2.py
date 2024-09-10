"""
Step 1:
Write a Python script that prompts the user for several numbers (when the user 
enter the string "stop", the script will stop prompting for numbers).
The numbers entered will be stored into a list one after the other.

Step 2:
After having retrieved all the numbers, print the list.

Step 3:
The script will then compute and print the minimum, the maximum and the mean 
of the different numbers present in the list.

Step 4:
Compute the "truncated mean" of the elements: 
the mean of all elements except the smallest and largest ones.

Example:
    if the list is:
    [3,4,3,6,77,3,77,55,45,45]
    
    the truncated mean will only take into account the elements:
    [4,6,55,45,45] (3 and 77 are ignored)
"""





numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1:
while True:
    answer=input("Enter an int or 'stop': ")
    if answer=='stop':
        break
    else:
        answer=int(answer)
        numbers.append(answer)
    
        # or 
        # numbers.append(int(answer))
     
        
# Step 2:
print(f"Here is the constructed list: {numbers} it's size is {len(numbers)}")
# or
print("Here is the constructed list:",numbers, "it's size is", len(numbers))

# Step 3:
if len(numbers) > 0: # If the list numbers is not empty
    # numbers=[3,4,1,5]
    mini=numbers[0] # 1
    maxi=numbers[0] # 5
    total=numbers[0] # 13
    # or
    # mini=maxi=total=numbers[0]
    
    for e in numbers[1:]: #[4,1,5]
        # e = 5
        if e < mini:
            mini=e
        if e > maxi:
            maxi=e
        total = total + e
        
    print(f"Minimum: {mini} Maximum: {maxi}")    
    print(f"Mean: {total/len(numbers)}")
else:
    print("The list is empty")    
    
if len(numbers) > 0:
    print(f"Minimum: {min(numbers)} Maximum: {max(numbers)}")    
    print(f"Mean: {sum(numbers)/len(numbers)}")
    # or
    import statistics
    print(f"Mean: {statistics.mean(numbers)}")
    
else:
    print("The list is empty")

# Step 4:
if len(numbers) > 0:
    # [3,4,3,6,77,3,77,55]
    org=numbers.copy() # <=> org=numbers[:]
    numbers.sort() # "in place"
    # [3,3,3,4,6,55,77,77]
    miniCount=numbers.count(numbers[0]) # 3
    maxiCount=numbers.count(numbers[-1]) # 2
    print(numbers)
    subList=numbers[miniCount:-maxiCount] # numbers[3:-2]
    print(subList)
    if len(subList) != 0:
        print(f"Truncated mean is {sum(subList)/len(subList)}")   
else:
    print("The list is empty")