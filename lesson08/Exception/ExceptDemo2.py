

x = 10

try:
    y = int(input('Please enter Number: '))
    z = x / y
except ZeroDivisionError as e:  # Exception as e 得到錯誤的訊息, Expection 是籠統的錯誤，可以更明確的指定用  ZeroDivisionError
    print('分母不可為0 ', e)
except ValueError as e:
    print('Error input type: ', e)
else:
    print(z)