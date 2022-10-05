from tkinter import *
import math
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    check_marks.config(text='')
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text='Break', bg=YELLOW, foreground=RED, font=(FONT_NAME, 35, 'bold'))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text='Break', bg=YELLOW, foreground=PINK, font=(FONT_NAME, 35, 'bold'))
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, 'bold'))
        count_down(works_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text= f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Work Timer')
window.minsize(width=500,height=400)
window.config(padx = 100, pady= 50,bg=YELLOW)



title_label = Label()
title_label.config(text='Timer', bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=2, row=1)

canvas = Canvas(width=200,height=224,bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00', fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=2,row=2)


start_button = Button(text='Start',width=7,height=1,bg='red')
start_button.grid(column=1,row=3)
start_button.config(command=start_timer)

reset_button = Button(text='Reset',width=7,height=1,bg='red')
reset_button.grid(column=3,row=3)
reset_button.config(command=reset_timer)

check_marks = Label()
check_marks.config(bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, 'bold'))
check_marks.grid(column=2, row=4)


window.mainloop()

