from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        window.attributes('-topmost', True)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(break_sec)
        window.attributes('-topmost', True)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)  # 4.8 = 4
    count_seconds = count % 60
    # print(f"count: {count} , mod = {seconds}")
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        checkmark_label.config(text=f"{'✔' * math.floor(reps / 2)}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=2, row=4)

window.mainloop()
