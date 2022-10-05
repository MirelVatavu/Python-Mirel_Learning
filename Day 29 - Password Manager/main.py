from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Password Generator Project
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)

    password_entry.clipboard_clear()

    password_entry.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():

    if len(website_entry.get()) == 0:
        messagebox.showerror(title='No Website', message="You can't have an empty website")
    elif len(email_entry.get()) == 0:
        messagebox.showerror(title='No Email', message="You can't have an empty mail")
    elif len(password_entry.get()) == 0:
        messagebox.showerror(title='No Password', message="You can't have an empty password")
    else:
        save = messagebox.askquestion(title=website_entry.get(),message=f'Are you sure you want to save the information?\nEmail: {email_entry.get()}\nPassword: {password_entry.get()} ')

        if save=='yes':
            with open('Data.txt','a') as f:
                f.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                messagebox.showinfo(title='Info', message='Your info is saved.')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

website_label = Label()
website_label.config(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label()
email_label.config(text='Email/Username:')
email_label.grid(column=0,row=2)

password_label = Label()
password_label.config(text='Password:')
password_label.grid(column=0,row=3)

website_entry = Entry()
website_entry.config(width=48)
website_entry.grid(pady=3, columnspan=2, column=1, row=1)
website_entry.focus()
email_entry = Entry()
email_entry.config(width=48)
email_entry.grid(pady=3, columnspan=2, column=1, row=2)
email_entry.insert(0,'myrellmq@gmail.com')

password_entry = Entry()
password_entry.config(width=29)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text='Generate Password',command=generate_pass)
generate_password_button.config(height=1, width=17)
generate_password_button.grid(pady=3, column=2, row=3)

add_button = Button(text='Add',width=47,command=save_pass)
add_button.grid(columnspan=2,column=1,row=4)

window.mainloop()