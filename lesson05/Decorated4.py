##未完成

def login(func, password):
    def check():
        if password == 1234:
            print('Succeed')
            func()
        else:
            print('Failed')
            return None
    return check

@login(password=1234)
def report():
    print("Secret: Today Top Line...")

report()
