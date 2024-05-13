from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}

#--------------------------- Read Data -----------------------
try:
    stored_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data  = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = stored_data.to_dict(orient="records")


current_card = {}
current_card = random.choice(words_to_learn)
print(current_card)


def flip_card():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(c_word, text=current_card["English"], fill="white")
    canvas.itemconfig(c_title, text="English", fill="white")
    canvas.itemconfig(c_image, image=back_image)
    flip_timer = window.after(3000, change_card)


def change_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    print(current_card)
    canvas.itemconfig(c_word, text=current_card["French"], fill="black")
    canvas.itemconfig(c_title, text="French", fill="black")
    canvas.itemconfig(c_image, image=front_image)
    flip_timer = window.after(3000, flip_card)


def is_know():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_card()

#--------------------------- UI -----------------------
window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
c_image = canvas.create_image(400, 263, image=front_image)
c_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
c_word = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)
r_image = PhotoImage(file="images/right.png")
button_r = Button(image=r_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=is_know)
button_r.grid(column=1, row=1)
w_image = PhotoImage(file="images/wrong.png")
button_w = Button(image=w_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=change_card)
button_w.grid(column=0, row=1)

window.mainloop()
