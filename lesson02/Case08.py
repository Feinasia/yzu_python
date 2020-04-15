# -*- coding:UTF-8 -*-

import math
n = int(input('請輸入數字'))
odd = n % 2 == 00
print("%d 是偶數嗎? %s" % (n, odd))

odd2 = math.fmod(n,2)==0
print("%d 是偶數嗎? %s" % (n, odd2))