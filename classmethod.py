# #use of class method and static method
# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#          return cls(name, date.today().year - year)
#
#     @staticmethod
#     def isAdult(age):
#          return  age > 18
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('Shubham', 2000)
# print(person1.age)
# print(person2.age)
# print(Person.isAdult(22))
#
# #empty function
# def fun():
#     pass
#
# #empty loop
# mutex = True
# while (mutex == True):
#     pass
#
# #empty in if/else
# mutex = True
# if (mutex == True):
#     pass
# else:
#     print("False")

# #generator
# def nextSquare():
#     i = 1
#     while True:
#         yield i*i
#         i += 1
#
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num, end=" ")

# returning multiple value
# using object
class Test:
    def __init__(self):
        self.str = 'geeksfogeeks'
        self.x = 20


def fun():
    return Test()


t = fun()
print(t.str)
print(t.x)


# using tuple
def fun():
    str = "geeksforgeeks"
    x = 20
    return (str, x)


a, b = fun()
print(a)
print(b)


# using list
def fun():
    str = "geeksforgeeks"
    x = 20
    return [str, x]


list = fun()
print(list)


# using dictionary
def fun():
    d = dict()
    d['str'] = 'geeksforgeeks'
    d['x'] = 20
    return d


dic = fun()
print(dic)

# partial function
from functools import partial


def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


g = partial(f, 3, 1, 4)
print(g(5))


#
from functools import *
def add(a, b, c):
    return 100 * a + 10 * b + c


add_part = partial(add, c=2, b=1)
print(add_part)

