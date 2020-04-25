import array
arr = array.array('i', [1,2,3])

print("the new created array is: ",end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

arr.append(4)
print("the append array is : ", end=" ")
for i in range(0, 4):
    print(arr[i], end=" ")
print()

arr.insert(2, 5)
print("the array after insertion is : ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print()

#pop and remove
arr = array.array('i',[1,2,3,1,5])
print("the new created array is: ",end=" ")
for i in range(5):
    print(arr[i], end=" ")
print()

print("the popped elment is: ",end=" ")
print(arr.pop(2));

print("\rthe array after popping is: ", end=" ")
for i in range(4):
    print(arr[i],end=" ")
print("\r")

arr.remove(1)
print("the array after removing is: ",end=" ")
for i in range(3):
    print(arr[i],end=" ")
print()

#index or reverse
arr = array.array('i',[1,2,3,2,1,5])
print("the new created array is: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")
print("\r")

print("the index of 1st occurrence of 2 is: ")
print(arr.index(2))

arr.reverse()
print("the array after reversing is: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")
print("\r")

#
arr = array.array('i',[1,2,3,1,2,5])
print("the datatype of array is :",end=" ")
print(arr.typecode)

print("\nthe itemsize of array is: ",end=" ")
print(arr.itemsize)

print("\nthe buffer info of array is : ",end=" ")
print(arr.buffer_info())

#
arr1 = array.array('i',[1,2,3,1,2,5])
arr2 = array.array('i',[1,2,3])

print("\nthe occurrences of 1 in array is: ",end=" ")
print(arr1.count(1))

arr1.extend(arr2)
print("\nthe modified array is: ",end=" ")
for i in range(0,9):
    print(arr1[i],end=" ")
print()

#
arr = array.array('i',[1,2,3,1,2,5])
l = [1,2,3]
arr.fromlist(l)
print("the modified array is: ",end=" ")
for i in range(9):
    print(arr[i],end=" ")
print("\r")

List = arr.tolist()

print("the new list created is: ",end=" ")
for i in range(0,len(List)):
    print(List[i],end=" ")
print("\r")

