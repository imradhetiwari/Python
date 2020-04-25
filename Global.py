# print(100 ** 100)
#
# #global variable
# def f():
#     print(s)
#
# s = "I love Geeksforgeeeks"
# f()
#
# #for same name
# def f():
#     s = "Me too."
#     print(s)
# s = "I love Geeksforgeeeks"
# f()
# print(s)
#
# #unbound local error
# def f():
#     print(s)
#     s = "me too."
#     print(s)
#
# s = "I love Geeksforgeeeks"
# f()
# print(s)

#global
def f():
    global s
    print(s)
    s = "looks for Geeksforgeeks python section."
    print(s)
s = "Python is Great!"
f()
print(s)

#1
a = 1
def f():
    print("inside f() :", a)

def g():
    a = 2
    print("inside g() :", a)

def h():
    global a
    a = 3
    print("inside h() : ", a)

print("global : ",a)
f()
print("global : ",a)
g()
print("global : ",a)
h()
print("global : ",a)