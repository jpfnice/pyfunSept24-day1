# Creation
l2=[67,89,19]
print(l2, len(l2))

l2=[True,False,"Hello",3.4,[6,7,8]]
print(l2, len(l2))

l2=list() # <=> l2=[] an empty list is created
print(l2, len(l2))

l2=list("abcdef")
print(l2, len(l2))

# Update of the list
l2=[67,89,19]
print(l2, len(l2))
# 
l2[0]=99
print(l2, len(l2))

size=len(l2)

l2.append(23) # append() is a method
print(l2, len(l2))

l2.insert(2,67) # insert() is a method
print(l2, len(l2))

l2.pop(0) # remove an element at a given position
l2.remove(89)
print(l2, len(l2))

l2.extend([6,7,8])
print(l2)
l2.sort()
print("Sorted list:",l2)
l2.append([6,7,8])
print(l2)




