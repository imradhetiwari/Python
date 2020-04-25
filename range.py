#return type
a = range(1, 10000)
print("The return type of range() is : ")
print(type(a))

#memory
import sys
a = range(1, 10000)
print("The size allotted using range() is : ")
print(sys.getsizeof(a))

#operations usage
r = range(1,6)
print("The list after slicing using range() : ")
print(r[2:6])


