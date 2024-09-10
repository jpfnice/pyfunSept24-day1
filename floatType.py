"""
basic Python types: int, float, complex, bool, NoneType

Datatype "float"
"""

nb1 = -103.34 # fixed notation
print(nb1, type(nb1))

nb1 = -103. # fixed notation
print(nb1, type(nb1))

nb1 = float("234.56")
print(nb1, type(nb1))

nb1 = float(23)
print(nb1, type(nb1))

nb1 = float()
print(nb1, type(nb1))

nb1 = 0.5E+12 # scientific notation
print(nb1, type(nb1))

nb1 = -1.332e-8 # scientific notation
print(nb1, type(nb1))

print(34E+128 * 10.E350)
