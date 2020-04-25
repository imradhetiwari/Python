# #functions are object
# def shout(text):
#     return text.upper()
#
# print(shout("Hello"))
#
# yell = shout
# print(yell("Hello"))
#
# #functions can be passed as arguments to other functions
# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(func):
#     greeting = func("Hi, I am created by a function passed as an argument")
#     print(greeting)
#
# greet(shout)
# greet(whisper)
#
# #functions can return another function
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
#
# add_15 = create_adder(15)
# print(add_15(20))

# *args and **kwargs
def myFun(arg1, *argv):
    print("First argument : ", arg1)
    for arg in argv:
        print("Next argument through *argv : ", arg)

myFun('Hello', 'Welcome', 'To', "GeeksforGeeks")

#
def myfun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

myfun("HI", first = 'Geeks', mid = 'For', last = 'Geeks')

#
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)

#
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myFun('geeks', 'for', 'geeks', first = "Geeks", mid = "For", last = "Geeks")

