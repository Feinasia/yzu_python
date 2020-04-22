import random as r
while True:
    n = r. randint(1, 100)

    if n == 50:
        print(n)
        break  # while 的中斷 code
    if n % 3 != 0:
        continue  #重新開始下一個迴圈

    print(n)