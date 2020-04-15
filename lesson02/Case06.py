# -*- coding:UTF-8 -*-

exchange = 29.123
print('%9.4f' % exchange) # 9:至少9個位數 含小數點1位  不足前面補 空白, 4:4位小數 不足後面補0
exchange = 129.123
print('%9.4f' % exchange)
exchange = 9.123
print('%9.4f' % exchange)
print('%09.4f' % exchange) # 9:至少9個位數 含小數點1位  不足前面補 0, 4:4位小數 不足後面補0