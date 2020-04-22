s = "she sell sea shell on the sea shore"

print(s)
print('有 %d 個 s' % s.count('s'))
print('有 sea 這個字嗎? %d' % s.find('sea'))  # find 第幾個位置起始

# All english? (a-zA-Z)
# Tip: 先用 replace 去除空白 (空白不算英文)
print(s.replace(' ', '').isalpha())

# 大小寫互換
print(s.swapcase())