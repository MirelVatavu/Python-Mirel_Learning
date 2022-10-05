from tkinter import *


def button_click():
    calculate = float(input.get()) * 1.609
    label_calculate['text'] = round(calculate)

window = Tk()

window.minsize(height=100,width=100)
window.config(padx=30,pady=20)


button = Button(text='Calculate')
button.grid(column=1,row=2)
button.config(command=button_click)

label = Label()
label.grid(column=0,row=0)

label = Label(text='Miles')
label.grid(column=2,row=0)

label = Label(text='is equal to')
label.grid(column=0,row=1)

label = Label(text='Km')
label.grid(column=2,row=1)

input = Entry()
input.grid(column=1,row=0)
input.config(width=7)
label_calculate = Label(text='0')
label_calculate.grid(column=1,row=1)




window.mainloop()