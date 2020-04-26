#Displaying the keys Alphabetically
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")
    print("Keys are")
    for i in sorted(key_value.keys()):
        print(i, end=" ")

def main():
  dictionary()

if __name__ == "__main__":
    main()
print("\r")

#sorting the keys and values in alphabetical order using key
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task-2:-\nKeys and Values sorted in alphabetical order by the key")
    for i in sorted(key_value):
        print((i, key_value[i]),end=" ")

if __name__ == "__main__":
    dictionary()
print("\r")

#sorting the keys and values in alphabetical order using value
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task-3:-\nsorting the keys and values in alphabetical order using value")
    print(sorted(key_value.items(),key=
                 lambda kv:(kv[1], kv[0])))
dictionary()

#sorted by key
from collections import OrderedDict
dict = {'ravi':'10', 'rajnish':'9', 'sanjeev':'6'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

#working of sorted() and itemgetter
from operator import itemgetter

lis = [{'name': 'Nandini', 'age': 20},
       {'name': 'Manjeet', 'age': 18},
       {'name': 'Nikhil', 'age': 19}]

print("The list printed sorting by age : ")
print(sorted(lis, key = itemgetter('age')))
print("\r")

print("The list printed sorting by age and name : ")
print(sorted(lis, key = itemgetter('age', 'name')))
print("\r")

print("The list printed sorting by age in descending order :")
print(sorted(lis, key = itemgetter('age'), reverse= True))
print("\r")

#sorted with lambda
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print("The list printed sorting by age : ")
print(sorted(lis, key = lambda i: i['age']))
print("\r")

print("The list printed sorting by age and name :")
print(sorted(lis, key = lambda i: (i['age'], i['name'])))
print("\r")

print("The list printed sorting by age in descending order : ")
print(sorted(lis, key = lambda i: i['age'], reverse= True))

# #Find common elements in three sorted array
# from collections import Counter
#
# def commonElement(ar1, ar2, ar3):
#     ar1 = Counter(ar1)
#     ar2 = Counter(ar2)
#     ar3 = Counter(ar3)
#
#     resultDict = dict(ar1.items() & ar2.items() & ar3.items())
#     common = []
#
#     for (key, value) in resultDict.items():
#         for i in range(0, value):
#             common.append(key)
#
#     print(common)
#
# if __name__ == "__main__":
#     ar1 = [1, 5, 10, 20, 40, 80]
#     ar2 = [6, 7, 20, 80, 100]
#     ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#     commonElement(ar1, ar2, ar3)