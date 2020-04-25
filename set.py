#creating a set
s = set()
print("initial blank set:")
print(s)

s = {1,1,2,3,5,6,24,3,5}
print("\nsimple set: ")
print(s)

s = set("GeeksForGeeks")
print("\nset with the use of string:")
print(s)

string = 'GeeksForGeeks'
s = set(string)
print("\nset with use of an object:")
print(s)

s = set(["Geeks","For","Geeks","Geks"])
print("\nset with the use of list:")
print(s)

s = {"Geeks","For","Geeks"}
print("\n",s)

#adding element and tuple to the set
s.add(8)
s.add(9)
s.add((6,7))
print("\nset after addition of three element:")
print(s)

#adding elements using Iterator
for i in range(1,6):
    s.add(i)
print("\nset after addition of elements:")
print(s)

#use of update function
s = set([4,5,(6,7)])
s.update((10,12))
print("\nset after addition of elements using update:")
print(s)

#Accessing of elements in a set
s = {"Geeks","For","Geeks"}
print("\nelements of set:")
for i in s:
    print(i)

print("Geeks" in s)

#using remove() or discard() method
s = {1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12}
print("\ninitial set:")
print(s)

s.remove(5)
s.remove(6)
print("\nset after removal of the two element:")
print(s)

s.discard(8)
s.discard(9)
print("\nset after discarding  two element:")
print(s)

#using iterator method
for i in range(4):
    s.discard(i)
print("\nset after removing a range of elements:")
print(s)

s.pop()
print("\nset after popping an element: ")
print(s)

s.clear()
print("\nset after clearing all the elements:")
print(s)

s = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
fs = frozenset(s)
print("\nthe frozenset is:")
print(fs)

print("\nempty frozenset:")
print(frozenset())

