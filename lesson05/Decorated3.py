def make_dress(func):
    def dress():
        print("wear clothing")
        func()
    return dress

@make_dress
def out():
    print("I'm out")

out()