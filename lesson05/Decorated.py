def make_dress(func):
    def dress():
        print("wear clothing")
        func()
    return dress

def out():
    print("I'm out")

m= make_dress(out)
m()