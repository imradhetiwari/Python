# #function inside function
# def messageWithWelcome(str):
#
#     def addWelcome():
#         return "Welcome to "
#
#     return addWelcome() + str
#
# def site(site_name):
#     return site_name
#
# print(messageWithWelcome(site("GeeksforGeeks")))
#
# #decorator
# def decorate_message(fun):
#     def addWelcome(site_name):
#         return "Welcome to " + fun(site_name)
#     return addWelcome
#
# @decorate_message
# def site(site_name):
#     return site_name
# print(site("GeeksforGeeks"))
#
# #attach data
# def attach_data(func):
#     func.data = 3
#     return func
# @attach_data
# def add (x, y):
#     return x + y
#
# print(add(2, 3))
# print(add.data)
#
# #
# def hello_decorator(func):
#     def inner():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner
#
# def function_to_be_used():
#     print("This is inside the function !!")
#
# function_to_be_used = hello_decorator(function_to_be_used)
# function_to_be_used()
#
# #
# import time
# import math
#
# def calculate_time(func):
#
#     def inner(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken is : ",func.__name__, end - begin)
#     return inner
#
# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
#
# factorial(5)
#
# #function return the value
# def hello_decorator(func):
#     def inner(*args, **kwargs):
#         print("Before Execution")
#
#         returned_value = func(*args, **kwargs)
#         print("After Execution")
#         return returned_value
#     return inner
#
# @hello_decorator
# def Sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
# a, b = 1, 2
# print("Sum = ", Sum_two_numbers(a, b))
#
# #
# def decorator_fun(func):
#     print("Inside decorator")
#
#     def inner(*args, **kwargs):
#         print("Inside inner function")
#         print("Decorated the function")
#         func()
#     return inner
#
# @decorator_fun
# def fun_to():
#     print("Inside actual function")
#
# fun_to()
#
# #
# def decorator_fun(func):
#     print("Inside decorator")
#
#     def inner(*args, **kwargs):
#         print("Inside inner function")
#         print("Decorated the function")
#         func()
#     return inner
#
# def func_to():
#     print("Inside actual function")
#
# decorator_fun(func_to)()
#
# #decorators with parameter1
# def decorator(*args, **kwargs):
#     print("Inside decorator")
#     def inner(func):
#         print("Inside inner function")
#         print("I like ", kwargs['like'])
#         func()
#     return inner
#
# @decorator(like= 'geeksforgeeks')
# def my_func():
#     print("Inside actual function")
#
# #2
# def decorator_func(x, y):
#     def Inner(func):
#         def wrapper(*args, **kwargs):
#             print("I like GeeksforGeeks")
#             print("Summation of values - {}".format(x + y))
#             func(*args, **kwargs)
#         return wrapper
#     return Inner
#
# def my_fun(*args):
#     for ele in args:
#         print(ele)
#
# decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')

#factorial by recursion
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)
print(facto(5))

#using memoization
def memoize_factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return inner

@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)
print(facto(6))

