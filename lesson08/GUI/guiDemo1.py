import tkinter

win = tkinter.Tk()

win.title('My GUI') #標題
label = tkinter.Label(win, text='Hello')
label.pack(side=tkinter.LEFT)
label2 = tkinter.Label(win, text='Hello2')
label2.pack(side=tkinter.RIGHT)


win. geometry('300x300') # 視窗大小

win.mainloop()  #視窗存在是無窮迴圈
