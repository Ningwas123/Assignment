from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('410x530')

e = Entry(root, width = 50, borderwidth = 7, font = "aria 10 bold")
e.grid(row = 0, column = 0,columnspan = 3, padx = 10, pady = 10)

# Defining function.

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def b_equal():
    s_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(s_number))

def b_add():
    f_number = e.get()
    global f_num
    f_num = int(f_number)
    e.delete(0, END)


# Defining buttons.

b1 = Button(root, text = '1', padx =30, pady =20, command = lambda: button_click(1),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b2 = Button(root, text = '2', padx =30, pady =20, command = lambda: button_click(2),
            bg='grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b3 = Button(root, text = '3', padx =30, pady =20, command = lambda: button_click(3),
            bg='grey', fg = "black", activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b4 = Button(root, text = '4', padx =30, pady =20, command = lambda: button_click(4),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b5 = Button(root, text = '5', padx =30, pady =20, command = lambda: button_click(5),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b6 = Button(root, text = '6', padx =30, pady =20, command = lambda: button_click(6),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b7 = Button(root, text = '7', padx =30, pady =20, command = lambda: button_click(7),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b8 = Button(root, text = '8', padx =30, pady =20, command = lambda: button_click(8),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b9 = Button(root, text = '9', padx =30, pady =20, command = lambda: button_click(9),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b0 = Button(root, text = '0', padx =30, pady = 85, command = lambda: button_click(0),
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5,)
b_add = Button(root, text = '+', padx =30, pady =20, command = b_add,
               fg = "black", bg = 'lightgrey', activebackground = 'white', activeforeground = 'brown',font = "arial 15 ", width = 5, borderwidth =5)
b_clear = Button(root, text = 'CLEAR', padx =30, pady =20, command = button_clear,
                 fg = 'red', bg = 'lightgrey' , activebackground = 'brown', activeforeground = 'white', font = "arial 15 bold", width = 5, borderwidth =5)
b_equals = Button(root, text = '=', padx =95, pady =39,command =  b_equal,
                  fg = "black", bg = 'lightgrey', activebackground = 'white', activeforeground = 'brown',font = "lucida 15 bold", width = 5, borderwidth =5)


# adding buttons on screen

b1.grid(row = 3, column = 2)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 0)

b4.grid(row = 2, column = 2)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 0)

b7.grid(row = 1, column = 2)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 0)

b0.grid(row = 4, column = 0, rowspan = 2)
b_add.grid(row = 4, column = 1)

b_clear.grid(row = 4, column = 2)
b_equals.grid(row = 5, column = 1, columnspan = 2)

mainloop()



