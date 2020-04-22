# 終極密碼
import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 7

while True:
    guess = int(input('Please enter a number, %d ~ %d (Remaining %d times)' % (min, max, count)))


    if guess >= max or guess <= min:
        print('WRONG RANGE')
        continue
    count -= 1  # count=count-1
    if guess == ans:
        print ("Congratulation")
        break
    elif guess < ans:
        if count == 0:
            print("YOU LOSS")
            break
        min = guess
    elif guess > ans:
        if count == 0:
            print("YOU LOSS")
            break
        max = guess
