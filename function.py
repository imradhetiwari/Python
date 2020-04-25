#even or odd
def evenOdd(x):
    if(x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(5)
evenOdd(6)

#new reference
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

#
def myFun1(x):
    x = [20, 30, 40]

lst = [10, 11, 12, 14, 15]
myFun1(lst)
print(lst)

#
def myFun1(x):
    x = 20

x = 10
myFun1(x)
print(x)

#
def swap(x, y):
    temp = x
    x = y
    y = x

x = 3
y = 4
swap(x, y)
print("x = ",x)
print("y = ",y)

#
def myFun(x, y = 50):
    print("x: ",x)
    print("y: ",y)
myFun(10)

#keyword argument
def student(firstname, lastname):
    print(firstname, lastname)

student(firstname = 'Geeks', lastname = 'Practice')
student(lastname= 'Practice', firstname= 'Geeks')

#variable length argument
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#kargs
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

myFun(first = 'Geeks', mid = 'For', last= 'Geeks')

#Anonymous function
cube = lambda x : x*x*x
print(cube(8))





