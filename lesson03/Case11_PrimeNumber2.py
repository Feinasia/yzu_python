def isPrime(n):
    check = True
    for i in range(2, n//2 + 1, 1):
        if n % i == 0:
            check = False
            break
    return check

#印出質數
for i in range(2, 101):
    if isPrime(i):
        print(i)

# List 2~100 是否質數
for i in range(2, 101):
    print(i,"質數" if isPrime(i) else "")