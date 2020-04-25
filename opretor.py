#arithmetic operater
a = 9
b = 4

add = a + b
sub = a - b
mul = a * b
truediv = a / b
floordiv = a // b
mod = a % b
pow = a ** b
print("addition is", add)
print("subtraction is",sub)
print("multiplication is",mul)
print("division is",truediv)
print("floor division is",floordiv)
print("modulus is ",mod)
print("a^b is",pow)

#relational operator
a = 13
b = 33

print("\na > b is",a > b)
print("a < b is",a < b)
print("a == b is",a == b)
print("a != b is",a != b)
print("a >= b is",a >= b)
print("a <= b is",a <= b)

#logical operator
a = True
b = False

print("\na and b is",a and b)
print("a or b is",a or b)
print("not a is",not a)

#bitwise operator
a = 10
b = 4

print("\nbitwise AND operation : ",a & b)
print("bitwise OR operation : ",a | b)
print("bitwise NOT operation : ",~a)
print("bitwise XOR operation : ",a ^ b)
print("bitwise right shift operation : ",a >>2)
print("bitwise left shift operation : ",a << 2)

#Identity operator
a1 = 3
b1 = 3
a2 = "GeeksForGeeks"
b2 = "GeeksForGeeks"
a3 = [1, 2, 3]
b3 = [1, 2, 3]

print("\n",a1 is not b1)
print(a2 is b2)
print(a3 is b3)

#membership operator
x = 'Geeks For Geeks'
y = {3: 'a', 4: 'b'}

print("\n",'G' in x)
print('geeks' not in x)
print('Geeks' not in x)
print(3 in y)
print('b' in y,"\n")

#logical not
a = not True
b = not False
print(a)
print(b,"\n")

#bitwise not
a = True
b = False
print(~a)
print(~b,"\n")

