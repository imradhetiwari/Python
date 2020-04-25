#
s = "10010"
c = int(s,2)
print("after converting to integer base 2: ", end=" ")
print(c)

e = float(s)
print("after converting to float : ", end=" ")
print(e)

#
s = '4'

c = ord(s)
print("after converting character to integer: ",end=" ")
print(c)

c = hex(56)
print("after converting 56 to hexadecimal string : ",end=" ")
print(c)

c = oct(56)
print("after converting 56 to octal string: ",end=" ")
print(c)

s = "Geeks"

c = tuple(s)
print("after converting string to tuple: ",end=" ")
print(c)

c = set(s)
print("after converting string to set: ",end=" ")
print(c)

c = list(s)
print("after converting string too list: ",end=" ")
print(c)

#
a = 111
b = 2
tup = (('a', 1), ('f', 2), ('g', 3))

c = complex(a, b)
print("after converting integer to complex number: ",end=" ")
print(c)

c = str(a)
print("after converting integer to string: ",end=" ")
print(c)

c = dict(tup)
print("after converting tuple to dictionary: ",end=" ")
print(c)

