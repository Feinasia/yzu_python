import random as r

n = r.randint(1,10)
if n % 2 ==0:
    print("%d 偶數" % n)
else:
    print("%d 奇數" % n)

# 類似三元運算子的寫法
print("%d %s" % (n, "偶數" if n % 2 ==0 else "奇數"))

# 建構樹否是偶數的函式
def IsOdd(n):
    return "偶數" if n % 2 == 0 else "奇數"
print("%d %s" % (n, IsOdd(n)))
