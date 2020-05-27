import tkinter
from tkinter import ttk
from tkinter import messagebox

def submit():
    messagebox.showinfo('Summary:', "{0}".format(combo.get()))

win = tkinter.Tk()
win.geometry('400x300')

label= tkinter.Label(win, text='Item: ')

#fruits = ['apple','banana', 'mango', 'melonwater']
fruits = {'apple':50, 'banana':60, 'mango':80, 'melonwater':30}
combo = ttk.Combobox(win, values=list(fruits.keys()), state='readonly')  # readonly 不能亂打, disable 不給選
combo.current(0) #0 預設第一個

label2= tkinter.Label(win, text='Sugar:')

rdio1 =tkinter.Radiobutton(win, text='正常', value=1.0)
rdio2 =tkinter.Radiobutton(win, text='少糖', value=0.7)
rdio3 =tkinter.Radiobutton(win, text='半糖', value=0.5)
rdio4 =tkinter.Radiobutton(win, text='微糖', value=0.3)
rdio5 =tkinter.Radiobutton(win, text='無糖', value=0)

chk1 = tkinter.Checkbutton(win, text='去冰')
chk2 = tkinter.Checkbutton(win, text='袋子')

btn = tkinter.Button(win,text='結帳', command=submit)


#combo.pack()
label.grid(column=0, row=0, padx=10, pady=10, sticky='W')
combo.grid(column=0, row=0, padx=70, pady=10, sticky='W')
label2.grid(column=0, row=1, padx=10, pady=10, sticky='W')
rdio1.grid(column=0, row=1, padx=70, pady=10, sticky='W') # EWSN 東西南北
rdio2.grid(column=0, row=1, padx=130, pady=10, sticky='W')
rdio3.grid(column=0, row=1, padx=190, pady=10, sticky='W')
rdio4.grid(column=0, row=1, padx=250, pady=10, sticky='W')
rdio5.grid(column=0, row=1, padx=310, pady=10, sticky='W')
chk1.grid(column=0, row=2, padx=10, pady=10, sticky='W')
chk2.grid(column=0, row=2, padx=70, pady=10, sticky='W')
btn.grid(column=0, row=3, padx=10, pady=10, sticky='W')

win.mainloop()
