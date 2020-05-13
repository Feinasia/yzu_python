def message(text):
    text = 'Say: ' + text
    def print_message():
        print(text)
    return print_message  # 無(),  未執行


m1 = message('Hello')  # 執行得到權力 但未執行
m2 = message('Hi')

m1() #輸出已得結果
m2()