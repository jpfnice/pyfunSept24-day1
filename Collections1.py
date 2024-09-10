
"""
Collection: list, tuple, str, set, dict, array, ....
    Sequences: list, tuple, str, array
"""

# Collections: len(), for, in
# Sequences: [], [:], +, *

name="Maria" # a str
print(len(name))

for char in name: # for variable-name in collection
    print(char)
    
if "ri" in name: # if "ri" is a substring of name then:
    print("ri is in Maria")

data=[23,45,67,78,79,100,12] # a "list"

print(len(data))

for nb in data: # for variable-name in collection
    print(nb, nb**2, nb**3)
    
if 79 in data: # if 79 is present in the list data then:
    print("79 is in data")
    
    