# #missing value error
# d = {'a': 1, 'b': 2}
# print("The value associated with 'c' is : ")
# print(d['c'])

#demonstrate defaultdict
import collections

defdict = collections.defaultdict(lambda : "Key NOt Found")
defdict['a'] = 1
defdict['b'] = 2
print("The value associated with 'a' is :")
print(defdict['a'])
print("The value associated with 'c' is :")
print(defdict['c'])

