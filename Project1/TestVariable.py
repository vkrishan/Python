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
#Various String operators/operations
#  Slice -> [] ;;  Slice -> [start:end]  ;;  in  ;; not in  ;;  %  ;;  conacaternation->  +  ;; repeat->  *
#   replace()  ;;  upper()  ;; lower()  ;;  join()  ;; reversed(object)  ;; split(' ') ;; replace("This","That")
#

str1= "Learning Python"
str2= "This is AMERICA"

print(str1[1])
print(str1[1:10])   # start:end-1
print("i" in str1)
print("i" in str1[7:13])
print("z" not in str2)

print(str1+str2)
print(str1[0:5]*2)

str3=str2.replace("AMERICA", "INDIA")
print(str3)
str4=str2.replace(str2[8:], "ARGENTINA")
print(str4)

print(str1.upper())
print(str2.lower())

print(' '.join(reversed(str1)))
















