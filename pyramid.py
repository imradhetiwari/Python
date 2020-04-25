#1
def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
n = 5
pypart(n)

#2
def pypart1(n):
    myList = []
    for i in range(1, n + 1):
        myList.append("*" * i)
    print("\n".join(myList))

n = 5
pypart1(n)

#3
def pypart2(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

n = 5
pypart2(n)

#4
def triangle(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

triangle(6)

#5
def numpat(n):
    num = 1
    for i in range(0, n):
        num = 1
        for i in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
numpat(n)

#6
def numpat1(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
numpat1(n)

#7
def alphabet(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\r")
n = 6
alphabet(n)

#8
def contalpha(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print("\r")
n = 5
contalpha(n)

#chaining comparison
x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

#
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f
exp2 = a is d > f is not c
print(exp1)
print(exp2)

#else with for
for i in range(1, 4):
    print(i)
else:
    print("No Break")

#
for i in range(1, 4):
    print(i)
    break
else:
    print("No Break")

#if array consist of even number
def contains_even_number(l):
    for eleement in l:
        if eleement % 2 == 0:
            print("list contains an even number")
            break
    else:
        print("list does not contain an even number")

print("\nFor List 1:")
contains_even_number([1, 9, 8])
print("\nFor List 2:")
contains_even_number([1, 3, 5])

#
count = 0
while (count < 1):
    count = count + 1
    print(count)
    break
else:
    print("No Break")

#dictionary mapping
def numbers_to_strings(argument):
    switcher = {
        0: 'zero',
        1: 'one',
        2: 'two',
    }
    return switcher.get(argument, 'nothing')

if __name__ == "__main__":
    argument = 2
    print(numbers_to_strings(argument))
