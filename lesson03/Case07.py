text ='半徑=10'
#求圓面積

name, r = text.split("=")  # 切割下來的都是字串

print("%s 是 %d 的圓面積為 %.2f" % (name, int(r), int(r) * int(r) * 3.1415))