from tkinter import *

def button_clicked():
   label['text'] = input.get()

window = Tk()

window.title('Calculator')
window.minsize(width=600,height=300)

window.config(padx=20,pady=20)
#Label

label = Label(text='Im a Label',font=('Century Gothic',11,'normal'))
label['text'] = 'New Text'
label.grid(column=0,row=0)
label.config(pady=20,padx=20)
#Button

button = Button(text='Click me',command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text='New Button')
new_button.grid(column=2,row=0)
#Entry

input = Entry(width=10)
input.grid(column=3,row=3)


window.mainloop()