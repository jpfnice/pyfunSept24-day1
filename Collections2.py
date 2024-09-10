
"""
Collection: list, tuple, str, set, dict, array, ....
    Sequences: list, tuple, str, array
"""

# Collections: len(), for, in
# Sequences: [], [:], +, *

name="Maria" # a str

first=name[0] # first element
print(first)

last=name[-1] # last element
print(last)

sub=name[2:5] # a "slice" -> a sub-string
print(sub)

name=name + " Leoni"
print(name)

name="*-" * 10
print(name)

data=[23,45,67,78,79,100,12] # a "list"

first=data[0] # first element
print(first)

last=data[-1] # last element
print(last)

sub=data[2:5] # a "slice" -> a sub-list
print(sub)

data=data + [600,700]
print(data)

data=[0]*20

print(data)