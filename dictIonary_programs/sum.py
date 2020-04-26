#Sum of all items in dictionary
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#2
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
    return sum

dict = {'a': 100, 'b': 200, 'c': 400}
print("Sum :",returnSum(dict))

#3
def returnSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]

    return sum
dict = {'a': 100, 'b': 300, 'c': 500}
print("Sum :", returnSum(dict))

