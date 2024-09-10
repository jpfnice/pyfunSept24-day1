"""
basic Python types: int, float, complex, bool, NoneType

Datatype "int"
"""

nb1 = 103
print(nb1, type(nb1))

nb1 = int("234")
print(nb1, type(nb1))

nb1 = int(23.67)
print(nb1, type(nb1))

nb1 = int() # <=> nb1=0
print(nb1, type(nb1))

nb1 = 0b011100 # binary notation
print(nb1, type(nb1))

nb1 = 0o665 # octal notation
print(nb1, type(nb1))

nb1 = 0xFAA # hexadecimal notation
print(nb1, type(nb1))

# + - * / % // **

print(22%5)
print(22/5)
print(22//5)
print(3**3)


