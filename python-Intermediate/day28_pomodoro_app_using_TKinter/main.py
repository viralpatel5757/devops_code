# make a pomodoro timer which allows user to work for 25 minutes and then reminds to take short break for 5 minutes
# long break of 20 minutes comes after 4 working session
# IMP : we cannot use while loop here as window.mainloop() at the end of the code itself is loop and running while loop will put the code in infinity loop.

import tkinter
import math

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
    # timer_text = 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # make title_label "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    # reset check_marks
    check_mark.config(text="")
    # reset the reps
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Working", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)  # we cannot use round here as round(3.8) = 4, because we want just 3 here
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # to show timer as 0:05 instead of 0:5
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)  # after(delay in ms, function to call, *args)
    else:
        mark = ""
        start_timer()
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # here x=100 and y=112 , which are (x,y) coordinates
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = tkinter.Label(font=(FONT_NAME, 10), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# Buttons
start_button = tkinter.Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()



