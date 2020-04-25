#immutable targets
import operator
x = 5
y = 6
a = 5
b = 6

z = operator.add(a, b)
p = operator.iadd(x, y)

print("value after adding using normal operator: ",end=" ")
print(z)
print("value after adding using inplace operator: ",end=" ")
print(p)
print("value of first argument using normal operator: ",end=" ")
print(a)
print("value of first argument using inplace iperator: ",end=" ")
print(x)

#mutable targets
a = [1, 2, 3, 4, 5]
z = operator.add(a, [1, 2, 3])
print("\nvalue after adding using normal operator: ",end=" ")
print(z)
print("value of first argument using normal operator: ",end=" ")
print(a)

p = operator.iadd(a, [1, 2, 3])
print("value after adding using inplace operator: ",end=" ")
print(p)
print("value of first argument using inplace operator: ",end=" ")
print(a)
print("\r")

#
x = operator.iadd(2, 3)
print("the value after adding and assigning : ",end="")
print(x)

y = "geeks"
z = "forgeeks"
y = operator.iconcat(y, z)
print("the string after concatenation is : ",end="")
print(y)

x = operator.isub(2, 3)
print("the value after subtracting and assiging : ",end="")
print(x)

x = operator.imul(2, 3)
print("the value after multiplying and assiging : ",end="")
print(x)

x = operator.itruediv(2, 3)
print("the value after dividing and assign : ",end="")
print(x)

x = operator.ixor(10, 5)
print("the value after xoring and assigning : ",end="")
print(x)

x = operator.ipow(5, 4)
print("the value after exponentiating and assigning : ",end="")
print(x)

x = operator.ilshift(8, 2)
print("the value after bitwise left shift and assigning : ",end="")
print(x)

x = operator.irshift(8, 2)
print("the value after bitwise right shift and assigning : ",end="")
print(x)











