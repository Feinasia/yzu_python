# 函式 (有回傳值)
def add(x, y):
    sum = (x + y) * 1.03
    return sum

# 函式 (無回傳值) VOID
def addAndprint(x,y):
    sum = (x + y) * 1.03
    print(sum)
    return # 在末端可寫可不寫

print((1+2) * 1.03)
print((5+2) * 1.03)
print(add(1,2))
print(add(5,2))
addAndprint(1,2)

