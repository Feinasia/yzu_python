def message(text):
    text = 'Say: ' + text
    def print_message():
        print(text)
    return print_message

m1 = message('Hello')  # 已執行完得到結果 但未輸出
m2 = message('Hi')

m1() #輸出已得結果
m2()