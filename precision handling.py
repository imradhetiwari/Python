#
import math

a = 3.4536

print("The integral value of number is :")
print(math.trunc(a))

print("\nThe smallest integer greater than number is :")
print(math.ceil(a))

print("\nThe greatest integer smaller than number is :")
print(math.floor(a))

print("\nThe value of number till 2 decimal place(using %) :")
print('%.2f'%a)

print("\nThe value of number till 3 decimal place using format : ")
print('{0:.3f}'.format(a))

print("\nThe value of number till 2 decimal place using round : ")
print(round(a,2))

