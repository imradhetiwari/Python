#using enumerate
for key, value in enumerate(["The", "Big", "Bang", "theory"]):
    print(key, value)

#use zip
Q = ['name', 'colour', 'shape']
A = ['apple', 'red', 'a circle']
for q, a in zip(Q, A):
    print('What is your {}? I am {}'.format(q, a))

#use item
d = {'geeks': 'for', 'only': 'geeks'}
print("The key value pair using iteritems is : ")
for i, j in d.items():
    print(i,j)

#
king = {'Akbar': 'The Great', 'Candragupta': 'The Maurya', 'MOdi': 'The Game Changer'}
for key, value in king.items():
    print(key, value)

#using sorted
l = [1, 3, 5, 6, 2, 1, 3]
print("The list in sorted order is : ")
for i in sorted(l):
    print(i, end=" ")

print("\nThe list in sorted order without duplicate : ")
for i in sorted(set(l)):
    print(i, end=" ")
print("\r")

#
basket = ['guave', 'orange', 'apple', 'pear',
          'guava', 'banana', 'grape']
for fruit in sorted(set(basket)):
    print(fruit)

#using reversed
l = [1, 3, 5, 6, 2, 1, 3]
print("\nthe list in original order : ")
print(l,end=" ")
print("\nthe list in reversed order is : ")
for i in reversed(l):
    print(i, end=" ")
print("\r")

#
for i in reversed(range(1, 10, 2)):
    print(i, end=" ")


