'''

b_sub = Button(root, text = '-', padx =40, pady =20)
b_mul = Button(root, text = '*', padx =40, pady =20)
b_div = Button(root, text = '/', padx =40, pady =20)
b_del = Button(root, text = '<-', padx =40, pady =20)

b_sub.grid(root, row = 5, column = 1)
b_mul.grid(root, row = 6, column = 0)
b_div.grid(root, row = 6, column = 1)

b_del.grid(root, row = 7, column = 0)

button9 = Button(root, text = '9', bg = 'grey', fg = "black" ,font = "impact 15 ",  padx = 40, pady = 20, width = 5, borderwidth =5)
button9.grid(row = 1, column = 0)
button8 = Button(root, text = '8', bg = 'grey', fg = "black" ,font = ("impact", 15, "bold"),  padx = 40, pady = 20, width = 5, borderwidth =5)
button8.grid(row = 1, column = 1)
button7 = Button(root, text = '7', bg = 'grey', fg = "black" ,font = "lucida 15 bold",  padx = 40, pady = 20, width = 5, borderwidth =5)
button7.grid(row = 1, column = 2)




'''

from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('420x550')


e1 = Entry(root, width = 65, borderwidth = 8)
e1.grid(row = 0, column = 0, columnspan = 3)

b0 = Button(root, text = '0', padx =30, pady = 85,
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5,)

b1 = Button(root, text = '1', padx =30, pady =20,
            bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5,)
b2 = Button(root, text = '2', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b3 = Button(root, text = '3', padx =30, pady =20, bg = 'grey', fg = "black", activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b4 = Button(root, text = '4', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b5 = Button(root, text = '5', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b6 = Button(root, text = '6', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b7 = Button(root, text = '7', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b8 = Button(root, text = '8', padx =30, pady =20, bg = 'grey', fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)
b9 = Button(root, text = '9', padx =30, pady =20, bg = 'grey',
            fg = "black" , activebackground = 'lightgrey', activeforeground = 'grey',font = "lucida 15 bold", width = 5, borderwidth =5)

b_add = Button(root, text = '+', padx =30, pady =20,
               fg = "black", bg = 'lightgrey', activebackground = 'white', activeforeground = 'brown',font = "arial 15 ", width = 5, borderwidth =5)
b_clear = Button(root, text = 'CLEAR', padx =30, pady =20,
                 fg = 'red', bg = 'lightgrey' , activebackground = 'brown', activeforeground = 'white', font = "arial 15 bold", width = 5, borderwidth =5)
b_equals = Button(root, text = '=', padx =95, pady =39,
                  fg = "black", bg = 'lightgrey', activebackground = 'white', activeforeground = 'brown',font = "lucida 15 bold", width = 5, borderwidth =5)

b7.grid(row = 1, column = 2)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 0)

b4.grid(row = 2, column = 2)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 0)

b1.grid(row = 3, column = 2)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 0)

b0.grid(row = 4, column = 0, rowspan = 2)
b_add.grid(row = 4, column = 1)
b_clear.grid(row = 4, column = 2)
b_equals.grid(row = 5, column = 1, columnspan = 2)

mainloop()