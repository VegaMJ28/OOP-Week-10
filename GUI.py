import tkinter as tk
from tkinter import *

top = Tk()

top.geometry("700x700")




answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)

        else:
            answer.insert(tk.INSERT,x)

    except:
        answer.delete(1.0, END)




B1 = Button(top, text = "7", width = 10 ,height = 5, command=lambda: show("7"))
B1.place (x = 100, y = 150)

B2 = Button(top, text = "8", width = 10 ,height = 5, command=lambda: show("8"))
B2.place (x = 200, y = 150)

B3 = Button(top, text = "9", width = 10 ,height = 5, command=lambda: show("9"))
B3.place (x = 300, y = 150)

B4 = Button(top, text = "*", width = 10 ,height = 5, command=lambda: show("*"))
B4.place (x = 400, y = 150)

B5 = Button(top, text = "4", width = 10 ,height = 5, command=lambda: show("4"))
B5.place (x = 100, y = 250)

B6 = Button(top, text = "5", width = 10 ,height = 5, command=lambda: show("5"))
B6.place (x = 200, y = 250)

B7 = Button(top, text = "6", width = 10 ,height = 5, command=lambda: show("6"))
B7.place (x = 300, y = 250)

B8 = Button(top, text = "-", width = 10 ,height = 5, command=lambda: show("-"))
B8.place (x = 400, y = 250)

B9 = Button(top, text = "1", width = 10 ,height = 5, command=lambda: show("1"))
B9.place (x = 100, y = 350)

B10 = Button(top, text = "2", width = 10 ,height = 5, command=lambda: show("2"))
B10.place (x = 200, y = 350)

B11 = Button(top, text = "3", width = 10 ,height = 5, command=lambda: show("3"))
B11.place (x = 300, y = 350)

B12 = Button(top, text = "+", width = 10 ,height = 5, command=lambda: show("+"))
B12.place (x = 400, y = 350)

B13 = Button(top, text = "0", width = 10 ,height = 5, command=lambda: show("0"))
B13.place (x = 200, y = 450)

B13 = Button(top, text = ".", width = 10 ,height = 5, command=lambda: show("."))
B13.place (x = 300, y = 450)

B14 = Button(top, text = "=", width = 10 ,height = 5, command=lambda: show("="))
B14.place (x = 400, y = 450)

B15 = Button(top, text = "/", width = 10 ,height = 5, command=lambda: show("/"))
B15.place (x = 400, y = 50)


top.mainloop()