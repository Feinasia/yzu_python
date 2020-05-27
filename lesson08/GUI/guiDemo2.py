import tkinter

win = tkinter.Tk()

win.title('My GUI') #標題
label = tkinter.Label(win, text='Hello', fg='yellow', bg='red', font=('Arial', 12))
label2 = tkinter.Label(win, text='Hello2')
button1 = tkinter.Button(win, text='Hello3')
label4 = tkinter.Label(win, text='Hello4')
button2 = tkinter.Button(win, text='Hello5')
label.grid(column=0, row=0, padx=20, pady=20)  #pad 留白
label2.grid(column=1, row=0)
button1.grid(column=1, row=1)
label4.grid(column=2, row=2)
button2.grid(column=2, row=0)

win. geometry('300x300') # 視窗大小

win.mainloop()  #視窗存在是無窮迴圈
