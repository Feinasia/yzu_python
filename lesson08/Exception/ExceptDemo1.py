import sys
import traceback

x = 10
y = int(input('Please enter Number: '))
try:
    z = x / y
except Exception as e:  # Exception as e 得到錯誤的訊息, Expection 是籠統的錯誤，可以更明確的指定用  ZeroDivisionError
    print('Error exist:', e)
    print(e.__class__.__name__)  # 得到錯誤的型態--> ZeroDivisionError
    cl, exc, tb = sys.exc_info()  # 錯誤資料運錫/位置
    lastCallStack = traceback.extract_tb(tb)[-1]
    print(lastCallStack)
else:
    print(z)