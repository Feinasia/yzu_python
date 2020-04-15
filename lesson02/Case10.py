# -*- coding:UTF-8 -*-
import math

x1, y1 = 10, 20
x2, y2 = 30, 40
# 求2點間的距離 d
d= ((x1-x2)**2 + (y1-y2)**2)**0.5
d1=math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))
print(d)
print(d1)
