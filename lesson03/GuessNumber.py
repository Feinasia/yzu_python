import random as r
ans = r.randint(1, 99)
min = 0
max = 100

while True:
    guess = int(input('Please enter a number, %d ~ %d' % (min, max)))
    if guess > max or guess < min:
        print('WRONG RANGE')
        continue

    if guess == ans:
        print ("Congratulation")
        break
    elif guess < ans:
        min = guess
    elif guess > ans:
        max = guess
