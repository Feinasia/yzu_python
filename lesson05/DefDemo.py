def add(x=1, y=2, z=None):
    if z == None:
        return x + y
    return (x + y) * z

print(add())
print(add(10))  # x=10  ,y as default
print(add(y=10)) # y=11, x as default
print(add(10, 20, 2))