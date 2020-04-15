import random

r = random.randrange(0, 2)  #<= r <2
print(r)

r = random.randint(0,2) #0<= r <=2
print(r)

# 電腦選號四星彩
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)

#跳脫字元
print("\"") # 跳脫字元 \, 印出 雙引號"，而不是文字外框
print("A\nB\tC")  # 換行 \n, 加一個 TAB \t

a = 100 + 200\
    - 50 * 5\
    / 10        #連接 續行符號 \
print(a)
