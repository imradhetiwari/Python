#
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("dictionary with the use of Integer keys:")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1,2,3,4]}
print("\ndictionary with use of mixed key:")
print(Dict)

#empty dictionary
Dict = {}
print("\nEmpty dictionary:")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\ndictionary with use of dict():")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\ndictionary with each item as a pair:")
print(Dict)

#nested dictionary
Dict = {1: 'Geeks', 2: 'For', 3:{'A': 'Welcome','B': 'To','C': 'Geek'}}
print("\nnested dictionary: ")
print(Dict)

#adding element
d = {}
print("\nEmpty dictionary:")
print(d)

d[0] = 'Geeks'
d[2] = 'For'
d[3] = 1
print("\ndictionary after adding three elements:")
print(d)

d['Value_set'] = 2,3,4,5
print("\ndictionary after adding three elements:")
print(d)

d[2] = 'Welcome'
print("\nupdated key value:")
print(d)

d[5] = {'Nested': {'1': 'Life', '2':'Begin'}}
print("\nadding a nested key:")
print(d)

#accessing element
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\naccessing a element using key:")
print(d['name'])
print("\naccessing a element using key:")
print(d[1])

print("\naccessing a element using get:")
print(d.get(3))

d = {0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4, 5), 5: {'Nested': {'1': 'Life', '2': 'Begin'}}}
print("\naccessing element of nested dictionary:")
print(d[5]['Nested']['1'])
print(d[3])
print(d['Value_set'])

#deletion
d ={5: 'Welcome', 6: 'To', 7: 'Geeks',
    'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
    'B': {1: 'Geeks', 2: 'Life'}}
print("\nintial dictionary:")
print(d)

del d[6]
print("\ndeleting a specific key:")
print(d)

del d['A'][2]
print("\ndeleting a key from nested dictionry:")
print(d)

#using pop()
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.pop(1)
print("\ndictionary after deletion :" + str(Dict))
print("\ndictionary after deletion:")
print(Dict)
print("\nvalue associated to poped key is: " + str(pop_ele))

#using popitem()
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

#using clear()
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
Dict.clear()
print("\ndeleting entire dictionary:")
print(Dict)

