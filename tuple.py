tup = ()
print("initial empty value: ")
print(tup)

tup = ('Geeks','For')
print("\ntuple with the use of string:")
print(tup)

l = [1,2,3,4,5]
print("\ntuple using list:")
print(tuple(l))

tup = tuple("Geeks")
print("\ntuple with use of function:")
print(tup)

#creating a tuple
tup = (5,'welcome',7,'Geeks')
print("\ntuple with mixed datatypes:")
print(tup)

tup1 = (1,2,3,4)
tup2 = ('Python','Geeks')
tup = (tup1,tup2)
print("\ntuple with nested tuple:")
print(tup)

tup = ('Radhe',) * 3
print("\ntuple with repetition:")
print(tup)

tup = ('Geeks')
n = 5
print("\ntuple with a loop:")
for i in range(int(n)):
    tup = (tup,)
    print(tup)

#accessing tuple with indexing
tup = tuple('Geeks')
print("\nfirst element of tuple: ")
print(tup[1])

#tuple unpacking
tup = ('Geeks','For','Geeks')
a,b,c = tup
print("\nvalues after unpacking: ")
print(a)
print(b)
print(c)

#concatenation of tuple
tup1 = (1,2,3,4)
tup2 = ('Geeks','For','Geeks')
tup3 = tup1 + tup2
print("\ntup1:")
print(tup1)
print("\ntup2: ")
print(tup2)
print("\ntuples after concatenation:")
print(tup3)

#slicing of tuple
tup = tuple('GEEKSFORGEEKS')
print("\nremoval of first element: ")
print(tup[1:])

print("\ntuple after sequence of element reverse:")
print(tup[::-1])

print("\nprinting elements between range 4-9:")
print(tup[4:9])

del tup
print(tup)
