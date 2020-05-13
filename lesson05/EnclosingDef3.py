def message(text):
    text = 'Say: ' + text
    def print_message():
        print(text)
    return print_message()  # 有() 會直接執行

m1 = message('Hello')  # 已執行完得到結果
m2 = message('Hi')
