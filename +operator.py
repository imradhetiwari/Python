#
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]

print(list1)
print(list2)

#
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

print("\n",list1)
print(list2)
print("\r")

# is and == operator
list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

#
list1 = []
list2 = []

print(id(list1))
print(id(list2))

#membership operator
list1=[1,2,3,4,5]
list2=[6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")

#
def overlapping(list1, list2):
    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if (list1[i] == list2[j]):
                return 1
    return 0


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
if (overlapping(list1, list2)):
    print("overlapping")
else:
    print("not overlapping")

#
x = 24
y = 20
list = [10, 20, 30, 40, 50];

if (x not in list):
    print( "x is NOT present in given list")
else:
  print("x is  present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#identity operator
x = 5
if (type(x) is int):
    print ("true")
else:
    print ("false")

#
x = 5.2
if (type(x) is not int):
    print ("true")
else:
    print ("false")

