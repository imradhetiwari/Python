#
a, b = 10, 20
min = a if a < b else b
print(min)

#
a, b = 10, 20
print((b, a)[a < b])
print({True: a, False: b}[a < b])
print((lambda: b, lambda: a)[a < b]())

#
a, b = 10, 20
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a ")

#nested ternary operator
a, b = 10, 20
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")

#conditional operator
a, b = 10, 20
min = a < b and a or b
print(min)

#division operator
print(5 / 2)
print(-5 / 2)
print(5 // 2)
print(-5 // 2)
print(5.0 // 2)
print(-5.0 // 2)
