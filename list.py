#multi dimenssional list
list = [['Geeks','For'],['Geeks']]
print("multidimensional list : ")
print(list)

#addition to a list by using append
l = []
print("print initial list: ")
print(l)

l.append(1)
l.append(8)
l.append(2)
print("\nlist after adding three element: ")
print(l)

for i in range(3,7):
    l.append(i)
print("\nlist after addition of elements in a range:")
print(l)

l.append((5,6))
print("\nlist after addition of tuple:")
print(l)

list = ['for','Geeks']
l.append(list)
print("\nlist after adding of a list:")
print(l)

#using insert method
l = [1,1,2,3,4]
print("\ninitial list:")
print(l)

l.insert(3,12)
l.insert(0,'Geeks')
print("\nlist after performing insert option:")
print(l)

#using extend method
l.extend([8,'Geeks','Always'])
print("\nlist after performing extend operation:")
print(l)

#accessing element from list
l = [2,3,4,5,['Geeks','For'],['Geeks']]
print("\naccessing element from list:")
print(l[1])
print(l[3])
print(l[4][1])
print(l[5][0])

#using remove opertion
list = [1,2,3,4,5,5,6,7,88,5,6,8,9,0,4,5,6]
print("\ninitial list:")
print(list)

list.remove(5)
list.remove(8)
print("\nlist after removal of two element:")
print(list)

for i in range(1,5):
    list.remove(i)
print("\nlist after removal a range of list:")
print(list)

#using pop method
list = [1,2,3,4,5]
list.pop()
print("\nlist after popping an element:")
print(list)

list.pop(2)
print("\nlist after popping a specific element:")
print(list)

#slicing
list = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("\ninitial list:")
print(list)

sliced_list = list[3:8]
print("\nslicing element in range 3-8:")
print(sliced_list)

sliced_list = list[5:]
print("\nslicing from 5th element till end:")
print(sliced_list)

sliced_list = list[:]
print("\nprinting all elements using slice operation :")
print(sliced_list)

sliced_list = list[:-6]
print("\nelements sliced till 6yh element:")
print(sliced_list)

sliced_list = list[-6:-1]
print("\nelement sliced from index -6 to -1:")
print(sliced_list)

sliced_list = list[::-1]
print("\nprinting list in reverse:")
print(sliced_list)
