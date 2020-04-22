# 某數 n  是否是質數
n = int(input("Please enter a number:"))
half = n//2
check = True
for i in range(2, half+1, 1):
    # print log
    print ('%d / %d  餘數 %d' % (n, i, n % i))
    if n % i == 0:
        check = False
        break

print(n, check)
