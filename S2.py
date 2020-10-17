from tkinter import *


window = Tk()
window.title("Wight Converter")

def kilo_c():
    gram = float(e1_val.get())*1000
    pound = float(e1_val.get())*2.20462
    ounces = float(e1_val.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

b1 = Button(window, text="Convert", command=kilo_c)
b1.grid(row=0, column=5)

lab1 = Label(window, text="KG")
lab1.grid(row=0, column=2)
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=3)
lab2 = Label(window, text="Grams")
lab2.grid(row=1, column=0)
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)
lab3= Label(window, text="Pounds")
lab3.grid(row=1, column=2)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=3)
lab4 = Label(window, text="Ounces")
lab4.grid(row=1, column=4)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=5)
window.mainloop()