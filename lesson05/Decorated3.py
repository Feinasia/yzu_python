def make_dress(func):
    def dress():
        print("wear clothing")
        func()
    return dress

def make_shoes(func):
    def shoes():
        print("wear shoes")
        func()
    return shoes

@make_dress
@make_shoes
def out():
    print("I'm out")

out()