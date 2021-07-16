from tkinter import *

root = Tk()
root.geometry('400x500')

def clicked():
    labelf = e1.get() + ' ' + e2.get()
    # .get() works only on ENTRY not on LABEL

    label2 = Label(root, text = labelf)
    label2.grid(row = 3, column = 1)

name = Label(root, text = 'NAME')
name.grid(row = 0, column = 0)
e1 = Entry(root, width = 20, borderwidth = 2)
e1.grid(row =0 , column = 1)

caste = Label(root, text = 'CASTE')
caste.grid(row =1 , column = 0)
e2 = Entry(root, width = 20, borderwidth = 2)
e2.grid(row =1 , column = 1)

button1 = Button(root, text = 'CLICK', command = clicked)
button1.grid(row = 2, column = 1)

mainloop()