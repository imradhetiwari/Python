# #iterator functions
# import itertools
# import operator
#
# l1 = [4, 6, 7, 1, 8]
# l2 = [1, 6, 5, 9]
# l3 = [8, 10, 5, 4]
# l4 = [l1, l2, l3]
#
# print("The sum after each itration is : ")
# print(list(itertools.accumulate(l1)))
#
# print("\n The product after each iteration is :")
# print(list(itertools.accumulate(l1, operator.mul)))
#
# print("\nPrint values in mentioned chain are : ")
# print(list(itertools.chain(l1, l2, l3)))
#
# print("\nAll values in mentioned chain are : ")
# print(list(itertools.chain.from_iterable(l4)))
#
# print("\nThe compressed values in string are : ")
# print(list(itertools.compress('GEEKSFORGEEKS',[1,0,0,1,0,0,1,1,0,0,1,0,1])))
#
# print("\nThe values after condition return false : ")
# print(list(itertools.dropwhile(lambda x : x%2 == 0,l1)))
#
# print("\nThe values that return false to function are : ")
# print(list(itertools.filterfalse(lambda x : x%2 == 0,l1)))
#
# #
# li1 = [2, 4, 5, 7, 8, 10, 20]
# li2 = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (10,11, 1)]
#
# print("\nThe sliced list values are : ")
# print(list(itertools.islice(li1,1, 6, 2)))
#
# print("\nThe values according to function are : ")
# print(list(itertools.starmap(min, li2)))
#
# print("\nThe list values till 1st false value are :")
# print(list(itertools.takewhile(lambda x : x%2 == 0, li1)))
#
#
# it = itertools.tee(li2, 3)
# print("\nThe iterators are : ")
# for i in range(0, 3):
#     print(list(it[i]))
#
# print("\nThe combined values of iterables is : ")
# print(*(itertools.zip_longest('Radhe', 'Krishna', fillvalue ='_')))
#
# print("\nThe cartesian product of the container is : ")
# print(list(itertools.product('AB','12')))
#
# print("\nAll the permutations of the given container is : ")
# print(list(itertools.permutations('GfG',2)))
#
# print("\nAll the combination of container in sorted order without replaement is : ")
# print(list(itertools.combinations('123',2)))
#
# print("\nAll the combination of container in sorted order with replacement is : ")
# print(list(itertools.combinations_with_replacement('123',2)))
#
# print("\nPrinting the number repeatedly : ")
# print(list(itertools.repeat('Radhe',4)))

#basic use of iter()
listA = ['a', 'e', 'i', 'o', 'u']
iter_listA = iter(listA)
try:
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
except:
    pass

#
lst = [11, 22, 33, 44, 55]
iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break

#
listB = ['Cat', 'Bat', 'Sat', 'Mat']
iter_listB = iter(listB)
try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
except:
    print("\nThrowing 'StopIteration' I cannot count more.")

#using oops
class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1

if __name__ == '__main__':
    a, b = 2, 5

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    print("\nPrint the range without iter()")

    for i in c1:
        print("Eating more Pizzas, counting ",i,end="\n")
    print("\nPrint the range using iter()\n")

    obj = iter(c2)
    try:
        while True:
            print("Eating more Pizzas, counting ",next(obj))
    except:
        print("\nDead on overfood, GAME OVER")

#iteration
for city in ['Berlin', 'Vienna', 'Zurich']:
    print(city)
print("\n")

for city in ('Python', 'Perl', 'Ruby'):
    print(city)
print("\n")

for char in "Iteration is easy":
    print(char, end=" ")
print("\r")

#
cities = ['Berlin', 'Vienna', 'Zurich']
iterator_obj = iter(cities)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

#
def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

for element in [34, [4, 5], (4, 5), {'a': 4}, "Radhe", 4.5]:
    print(element, "is iterable : ",iterable(element))

#generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

#
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()
print(x.__next__())
print(x.__next__())
print(x.__next__())

#fibbanacci series
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

print("\nusing for in loop")
for i in fib(50):
    print(i,end=" ")

#
def generator():
    t = 1
    print("\nFirst result is ",t)
    yield t

    t += 1
    print("second rsult is ",t)
    yield t

    t += 1
    print("Third result is ",t)
    yield t

call = generator()
next(call)
next(call)
next(call)

#
print("\nThe square root of first 10 numbers : ")
generator = (num ** 2 for num in range(11))
for num in generator:
    print(num,end=" ")

print("\r")

#string
string = 'Geeks'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)


