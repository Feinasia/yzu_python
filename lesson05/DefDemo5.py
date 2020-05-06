x = 0  # globe var
y = 0 # globe var
z=[0]
def changeX(n):
    x = n   # Local var

print('x=', x)
changeX(100) # 因 globe var =/= Local var
print('x=', x)


def changeY(n):
    global y
    y = n   # Local var

changeY(50)
print('y=', y)


def changeZ(m, n):
    m[0]=n

print('z=', z)
changeZ(z, 100)
print('z=', z)

