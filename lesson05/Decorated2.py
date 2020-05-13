def login(func, password):
    def check():
        if password == 1234:
            print('Succeed')
            func()
        else:
            print('Failed')
            return None
    return check


def report():
    print("Secret: Today Top Line...")

report()
login(report, int(input("Please enter password: ")))()