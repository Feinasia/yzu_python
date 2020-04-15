import keyword
# -*- coding:UTF-8 -*-
print("測試中文")

if 2<0:
    print("A")
    print("B")
else:
    print("C")
    print("D")
print("E")

a = 100    #十進位為預設
b = 0b100  #二進位
c = 0o12   #八進位
d = 0x12   #十六進位
print(a, b, c, d)

# 型態
a = 10    #int
b= 3.14   #float
c = 1+2j  #complex 複數
print(type(a), type(b), type(c))

#變數初始值
#age = 18
#name = "Vincent"
age, name = 18, "Vincent"
print (age, name)

#flag
check = True
print(check, type(check))

score = 55
mark = score>= 60
print(mark, type(mark))

#保留字
#import keyword 在最前面
kw = keyword.kwlist
print(kw)

#刪除變數
a = 10
print(a)
del a
print(a)