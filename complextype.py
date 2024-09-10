"""
basic Python types: int, float, complex, bool, NoneType

Datatype "complex"

"""

nb = 123

nb1 = 3.4+3.5j
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)

nb1 = 4.5j 
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)

nb1 = complex(2.3, 6.7) # a complex "constructor"
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)


nb1 = complex()
print(nb1, type(nb1))
print(nb1.real)
print(nb1.imag)


