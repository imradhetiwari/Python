#
import operator
a = 13
b = 3

print("the addition of numbers is : ",end="")
print(operator.add(a, b))
print("the difference of numbers is : ",end="")
print(operator.sub(a, b))
print("the product of numbers is : ",end="")
print(operator.mul(a, b))
print("the true division of numbers is : ",end="")
print(operator.truediv(a, b))
print("the floor division of number is : ",end="")
print(operator.floordiv(a, b))
print("the exponentiation of number is : ",end="")
print(operator.pow(a, b))
print("the modulus of numbers is : ",end="")
print(operator.mod(a, b))
print()

if(operator.lt(a, b)):
    print("a is less than b")
else:
    print("a is not less than b")

if(operator.le(a, b)):
    print("a is less than or equal to b")
else: print("a is not less than or equal to b")

if(operator.eq(a, b)):
    print("a is equal to b")
else:
    print("a is not equal to b")

print()
if(operator.gt(a, b)):
    print("a is greater than b")
else:
    print("a is not greater than b")

if(operator.ge(a, b)):
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")

if(operator.ne(a, b)):
    print("a is not equal to b")
else:
    print("a is equal to b")

print("\r")

#
li = [1, 5, 6, 7, 8]
print("the originol list is : ",end="")
for i in range(0, len(li)):
    print(li[i],end=" ")

operator.setitem(li, 3, 3)
print("\nthe modified list after setitem() is : ",end="")
for i in range(0, len(li)):
    print(li[i],end=" ")

operator.delitem(li, 1)
print("\nthe modified list after delitem() is : ",end="")
for i in range(0, len(li)):
    print(li[i],end=" ")

print("\nthe 4th item of list is : ",end="")
print(operator.getitem(li,3))

#
li = [1, 5, 6, 7, 8]
print("\nthe original list is : ",end="")
for i in range(0,len(li)):
    print(li[i],end=" ")

operator.setitem(li,slice(1, 4),[2, 3, 4])
print("\nthe modified list after setitem() is : ",end="")
for i in range(0,len(li)):
    print(li[i],end=" ")

operator.delitem(li,slice(2, 4))
print("\nthe modified list after delitem() is : ",end="")
for i in range(0,len(li)):
    print(li[i],end=" ")

print("\nthe 1st and 2nd element of list is : ",end=" ")
print(operator.getitem(li,slice(0, 2)))

#
s1 = "geeksfor"
s2 = "geeks"
print("\nthe concatenated string is : ",end="")
print(operator.concat(s1, s2))

if(operator.contains(s1, s2)):
    print("geeksfor contain geeks")
else:
    print("geeksfor does not contain geeks")


#bitwise
a = 3
b= 4
print("\nthe bitwise and of a and b is : ",end="")
print(operator.and_(a, b))
print("the bitwise or of a and b is : ",end="")
print(operator.or_(a, b))
print("the bitwise xor of a and b is : ",end=" ")
print(operator.xor(a, b))
print("the inverted value of a is : ",end="")
print(operator.invert(a))