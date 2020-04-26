#Using del
test_dict = {'Arushi': 22, 'Anuradha': 11, 'Manjeet': 33, 'Maan': 44}
print("The dictionary before performing remove is :" + str(test_dict))
del test_dict['Maan']
print("The dictionary after remove is : " + str(test_dict))

#using pop()
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
print("The dictionary before performing remove is :" + str(test_dict))
removed_value = test_dict.pop('Mani')

print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))
print("\r")

removed_value = test_dict.pop('Manjeet', 'No key found')
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

#using item() + dict comprehension
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

print ("The dictionary before performing remove is : " + str(test_dict))
new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'}

print ("The dictionary after remove is : " + str(new_dict))




