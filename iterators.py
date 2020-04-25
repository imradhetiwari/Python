# #list
# cars = ['Aston', 'Audi', 'McLaren']
# i = 0
# while (i < len(cars)):
#     print(cars[i])
#     i += 1
# #
# print("\r")
# for name in cars:
#     print(name)
# #
# print("\r")
# for i in range(len(cars)):
#     print(cars[i])
# #
# print("\r")
# for i, x in enumerate(cars):
#     print(i, x)
# #
# print("\r")
# for x in enumerate(cars):
#     print(x[0], x[1])
# #
# print("\r")
# print(enumerate(cars))
# #
# print("\r")
# for x in enumerate(cars, start = 1):
#     print(x[0], x[1])
# print("\r")
# #
# cars = ['Aston', 'Audi', 'McLaren']
# accessories = ["GPS kit", "Car repair-tool kit Price"]
# prices = {1: '570000$', 2: '680000$', 3: '450000$', 4: '8900$', 5: '4500$'}
# for index, c in enumerate(cars, start = 1):
#     print("Car : %s Price : %s" %(c, prices[index]))
# for index, a in enumerate(accessories, start = 1):
#     print("Accessory : %s Price : %s" %(a, prices[index + len(cars)]))
#
# #zip
# cars = ['Aston', 'Audi', 'McLaren']
# accessories = ['GPS', 'Car repair kit', 'Dolby sound kit']
# for c, a in zip(cars, accessories):
#     print("Car : %s, Accessory required : %s" %(c, a))
#
# #
# l1, l2 = zip(*[('Aston', 'GPS'), ('Audi', 'Car Repair'),
#                ('McLaren', 'Dolby sound kit')
#                ])
# print(l1)
# print(l2)
#
#iterable user defined type
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration

        self.x = x + 1;
        return x

for i in Test(15):
    print(i)

for i in Test(5):
    print(i)
    
