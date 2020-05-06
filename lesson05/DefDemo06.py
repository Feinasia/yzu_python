def add(x):
    return x + 1

def sub(x):
    return x - 1
def operate(func, x):  # 函式拿來當參數
    return func(x)

x = 10
x = operate(sub, x)  # 函式拿來當參數
print(x)

y = 10
y = operate(add, y)  # 函式拿來當參數
print(y)

z = [add, sub] #函式陣列
for i in z:
    y = 10
    y = operate(i, y)
    print(y)



