# Data Types: Number, String, List, Tuple, Dictionary etc...

a=100           # Declare variable
print(a)
a="Hundred"     # Re-assign a
print(a)

# Concatenate variables of different data types

#ex: print(2+"two")  # RUNTIME error

b=2
c="Three"
print(str(b)+c) # Typecasting integer to string format

# Local and Global variable:

def aMethod():
    a="I am learning Python"  ## This value is local and dies within the method
    print(a)

aMethod()
print(a)

# using "global" keyword

def bMethod():
    global a
    print(a)
    a="I am learning Linux as well"    # changing global variable
    print(a)

bMethod()
print(a)

del a       # delete a variable

print(40*"*")

# STRINGS



















