#and gate
def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False

if __name__=='__main__':
    print(AND(1, 1))

print("+____________________+_________________+")
print("|  AND Truth Table   |     Result      |")
print("A = False, B = False | A AND B = ", AND(False, False),"|")
print("A = False, B = True  | A AND B = ", AND(False, True), "|")
print("A = True, B = False  | A AND B = ", AND(True, False), "|")
print("A = True, B = True   | A AND B = ", AND(True, True),  "|")
print()

#or gate
def OR(a, b):
    if a == 0 and b == 0:
        return False
    else:
        return True

if __name__=='__main__':
    print(OR(0, 0))

print("+____________________+_________________+")
print("|   OR Truth Table   |     Result      |")
print("A = False, B = False | A OR B = ", OR(False, False),"|")
print("A = False, B = True  | A OR B = ", OR(False, True), "|")
print("A = True, B = False  | A OR B = ", OR(True, False), "|")
print("A = True, B = True   | A OR B = ", OR(True, True),  "|")
print()

#NAND gate
def NAND(a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True

if __name__=='__main__':
    print(NAND(1, 1))

print("+____________________+_________________+")
print("|  NAND Truth Table  |     Result      |")
print("A = False, B = False | A NAND B = ", NAND(False, False),"|")
print("A = False, B = True  | A NAND B = ", NAND(False, True), "|")
print("A = True, B = False  | A NAND B = ", NAND(True, False), "|")
print("A = True, B = True   | A NAND B = ", NAND(True, True),  "|")
print()

#NOR gate
def NOR(a, b):
    if a == 0 and b == 0:
        return True
    else:
        return False

if __name__=='__main__':
    print(AND(0, 0))

print("+____________________+_________________+")
print("|  NOR Truth Table   |     Result      |")
print("A = False, B = False | A NOR B = ", NOR(False, False),"|")
print("A = False, B = True  | A NOR B = ", NOR(False, True), "|")
print("A = True, B = False  | A NOR B = ", NOR(True, False), "|")
print("A = True, B = True   | A NOR B = ", NOR(True, True),  "|")
print()

#NOT gate
def NOT(a):
    if a == 1:
        return False
    elif a == 0:
        return False

if __name__=='__main__':
    print(NOT(1))

print("+____________________+_________________+")
print("|  NOT Truth Table   |     Result      |")
print("A = False | NOT A = ", NOT(False),"|")
print("A = True  | NOT A = ", NOT(True), "|")
print()

#Ex-or gate
def Exor(a, b):
    if a != b:
        return True
    else:
        return False

if __name__=='__main__':
    print(AND(1, 1))

print("+____________________+_________________+")
print("|  EX-or Truth Table   |     Result      |")
print("A = False, B = False | A EX-or B = ", Exor(False, False),"|")
print("A = False, B = True  | A EX-or B = ", Exor(False, True), "|")
print("A = True, B = False  | A EX-or B = ", Exor(True, False), "|")
print("A = True, B = True   | A EX-or B = ", Exor(True, True),  "|")
print()

#EX-Nor gate
def ExNor(a, b):
    if a == b:
        return True
    else:
        return False

if __name__=='__main__':
    print(ExNor(1, 1))

print("+____________________+_________________+")
print("|  EX-Nor Truth Table   |     Result      |")
print("A = False, B = False | A EX-Nor B = ", ExNor(False, False),"|")
print("A = False, B = True  | A EX-Nor B = ", ExNor(False, True), "|")
print("A = True, B = False  | A EX-Nor B = ", ExNor(True, False), "|")
print("A = True, B = True   | A EX-Nor B = ", ExNor(True, True),  "|")