# #while loop
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")
#
# #else with while
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")
# else:
#     print("In Else Block")
#
# #iteration
# print("\nList Iteration")
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# print("\nTuple Iteration")
# t = ("geeks", "For", "Geeks")
# for i in t:
#     print(i)
#
# print("\nString iteration")
# s = "Geeks"
# for i in s:
#     print(i)
#
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print("%s %d" %(i, d[i]))
#
# #
# list = ["geeks", "for", "geeks"]
# for index in range(len(list)):
#     print(list[index])
#
# #else with for
# l = ["geeks", "for", "geeks"]
# for index in range(len(l)):
#     print(l[index])
# else:
#     print("Inside Else Block")
#
# #nested for
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=" ")
#     print()
#
# #continue
# for letter in "geeksforgeeks":
#     if letter == 'e' or letter == 'g':
#         continue
#     print("Current Letter : ",letter)

#break
for letter in 'geeksforgeeks':
    if letter == 'f' or letter == 'r':
        break
    print("current letter : ",letter)

#pass
for letter in 'geeksforgeeks':
    pass
print("last letter", letter)

