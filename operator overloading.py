# +, * operator for different purpose
print(1 + 2)
print("Geeks" + "For")
print(3 * 4)
print("Geeks" * 4)

#
class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a

ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

#
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a, self.b

ob1 = complex(1, 3)
ob2 = complex(2, 4)
ob3 = ob1 + ob2
print(ob3)

#
class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False

ob1 = A(2)
ob2 = A(3)
if(ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")

#
class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "NOt equal"

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)
print(ob3 == ob4)

#Any
print(any([False, False, False, False]))
print(any([False, True, False, False]))
print(any([True, False, False, False]))

#all
print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([True, True, True, False]))