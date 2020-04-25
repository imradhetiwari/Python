#unpacking
def fun(a,b,c,d):
    print(a,b,c,d)

my_list = [1,2,3,4]
fun(*my_list)

#
for i in  range(3,6):
   print(i,end=" ")
print()
args = [3, 6]
for i in range(*args):
    print(i,end=" ")
print()

#
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

print(mySum(1,2,3,4,5,6))
print(mySum(10, 20))

#
def fun1(a,b,c):
    print(a,b,c)

def fun2(*args):
    print(args)
    args = list(args)
    args[0] = 'Geeksforgeeks'
    args[1] = 'Awesome'
    fun1(*args)

fun2('Hello', 'beautiful', 'world!')

#
def fun(a,b,c):
    print(a,b,c)

d = {'a':2, 'b':4, 'c':10}
fun(**d)

#
def fun(**kwargs):
    print(type(kwargs))

    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

fun(name = "geeks", ID = "101", language = "Python")

#end parameter
print("Welcome to", end=" ")
print("GeeksforGeeks")

#
print("Python", end= '@')
print("GeeksforGeeks")

