# -*- coding:UTF-8 -*-
symbol = '2330,TW'
name = "TSMC"
price = 286.5
#shares = 5000
shares = int(input('請輸入股數 = '))

print('2330.TW TSMC 成交價 286.5 買進 5000股 (5張) 成本 1,432,500.0')
# %s(放字串) %d(放整數)  %f(放符點數) %.1f(1位小數)
print("%s %s 成交價 %.1f 買進 %d股 (%d張) 成本 %.1f" % (symbol, name, price, shares, shares/1000, price * shares))

