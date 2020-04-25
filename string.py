# #declaring a list
# l = [1,'a','string',1+3]
# print(l)
# l.append(6)
# print(l)
# l.pop()
# print(l)
# print(l[1])
#
# #itretion by while loop
# i = 1
# while i < 10:
#     print(i,end=" ")
#     i +=1
#
# #itretion by for loop
# s = "Hello World"
# for i in s:
#     print(i,end="")
# print()
#
# #itretion by for loop in list
# l = [1,3,4,6,8,8]
# for i in l:
#     print(i,end=' ')
# print()
#
# #itretion for range by for loop
# for i in range(0,10):
#     print(i,end=" ")
#
# #strings
# #1
# string = 'welcome to the Geeks World'
# print("\nstrings with the use of single quotes: ")
# print(string)
#
# #2
# string = "I'm a Geek"
# print("\nstring with the use of double quotes: ")
# print(string)
#
# #3
# str = '''I'm a Geek and I live in a world of "Geeks"'''
# print("\nstring with use of triple quotes:")
# print(str)
#
# #4
# str = '''Geeks
#      for
#         Life'''
# print("\ncreating a multiline string: ")
# print(str)
#
# #access character of string
# str = "GeeksForGeeks"
# print("initial string: ")
# print(str)
# print("\nFirst character of string: ")
# print(str[0])
# print("\nlast character of string: ")
# print(str[-1])
#
# #slicing operator
# str = "GeeksForGeeks"
# print("initial string: ")
# print(str)
# print("\nslicing characters from 3-12: ")
# print(str[3:12])
# print("\nslicing character between 3rd and 2nd last character: ")
# print(str[3:-2])
#
# #
# str = "hello, I'm Geek"
# print("initial string: ",str)
#   #updating the string
# str = "wlecome to the Geek's world"
# print("\nupdated string: ",str)

# #deleting entire string
# str = "hello, I'm Geek"
# print("initial string: ",str)
# del str
# print( "\ndeleting entier string:",str)
#
# #escape sequencing
# str = '''I'm "Geek"'''
# print("\ninitial string with use of triple quotes: ",str)
#
# str = 'I\'m a "Geek"'
# print("\nescaping single quotes: ",str)
#
# str = "I'm a \"Geek\""
# print("\nescaping double quotes: ",str)
#
# str = "C:\\Python\\Geeks\\"
# print("\nescaping backslashes: ",str)
#
# #ignore the escape sequence
# str = "THis is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nprinting in HEX with the use of escape sequence: ",str)
#
# str = r"THis is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nprinting Raw string in HEX format : ",str)
#
# #formatting
#     #default order
# str = "{} {} {}".format("Geeks","For","Life")
# print("\nprint string in default order:")
# print(str)
#
#     #positional formatting
# str = "{1} {0} {2}".format("Geeks","For","Life")
# print("\nprint string in positional order:")
# print(str)
#
#     #keyword formatting
# str = "{a} {b} {c}".format(a = "Geeks",b = "For",c = "Life")
# print("\nprint string in order of keword:")
# print(str)
#
# #formatting of integer
# str = "{0:b}".format(16)
# print("\nbinary representation of 16:")
# print(str)
# str = "{0:o}".format(16)
# print("\noctal representation of 16:")
# print(str)
# str = "{0:x}".format(16)
# print("\nhexadecimal representation of 16:")
# print(str)
# str = "{0:e}".format(165.465)
# print("\nexponent representation of 165.465:")
# print(str)
# #round off integers
# str = "{0:.3f}".format(1/6)
# print("\none-sixth is:")
# print(str)
#
# #string alignment
# str = "|{:<10}|{:^10}|{:>10}|".format('Geeks','For','Geeks')
# print("\nprint alignment with formatting: ")
# print(str)
#
# str = "\n{0:^16} was founded in {1:<4}".format("GeeksForGeeks","2009")
# print(str)
#
# #reversing the string
# #1using for loop
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s = "GeeksForGeeks"
# print("the originol string is : ",end="")
# print(s)
# print("the reversed string : ",end="")
# print(reverse(s))
#
# #2using recursion
# def reverse(s):
#     if len(s) == 0:
#         return  s
#     else:
#         return reverse(s[1:]) + s[0]
#
# s = "GeeksForGeeks"
# print("the originol string is : ",end="")
# print(s)
# print("the reversed string : ",end="")
# print(reverse(s))
#
# #3using extended slice syntax
# def reverse(str):
#     str = str[::-1]
#     return str
# s = "GeeksForGeeks"
# print("the originol string is : ",end="")
# print(s)
# print("the reversed string : ",end="")
# print(reverse(s))
#
# #4using reversed
# def reverse(str):
#     str = "".join(reversed(str))
#     return str
# s = "GeeksForGeeks"
# print("the originol string is : ",end="")
# print(s)
# print("the reversed string : ",end="")
# print(reverse(s))

#find duplicate
from collections import Counter
def find_dup_char(input):
    wc = Counter(input)
    j = -1
    for i in wc.values():
        j = j + 1
        if(i > 1):
            print(wc.keys(),[j])


input = 'geeksforgeeks'
find_dup_char(input)

