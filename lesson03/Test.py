# 雞兔同籠 (共83隻雞兔，共240隻腳)
n = 83
f = 240

c=0 #雞數
r=0 #兔數

r = (f - n * 2) / 2 # 腳的差異/2
c = n - r

print ("雞有 %d 隻, 兔子有 %d 隻" % (c, r))


def test(n, f):
    r = (f - n * 2) / 2
    c = (n * 4 - f) / 2
    return print("雞有 %d 隻, 兔子有 %d 隻" % (c, r))

test(83, 240)

