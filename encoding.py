#encoding
a = 'GeeksforGeeks'
c = b'GeeksforGeeks'
d = a.encode('ASCII')
if (d == c):
    print("Encoding successful")
else:
    print("Encoding unsuccessful")

#decoding
a = 'GeeksforGeeks'
c = b'GeeksforGeeks'
d = c.decode('UTF-8')
if (d == a):
    print("Decoding successful")
else:
    print("Decoding unsuccessful")

#swapping
x = 10
y = 20
print("the value of x is {} and y is {}".format(x, y))
x, y = y, x
print("After swapping values of x is {} and y is {}".format(x, y))