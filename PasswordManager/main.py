from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = random_letters + random_symbols + random_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = web_input.get()
    email = user_input.get()
    password = pass_input.get()
    new_data = {
        website:
            {
                "name": email,
                "password": password
            }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save.")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- Search ------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not Found Error")
    else:
        web = web_input.get()
        if web in data:
            search = data[web]
            messagebox.showinfo(title=web, message=f"email: {search['name']} \npassword: {search['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details Found For {web}")
    finally:
        web_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)

web_input = Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()
user_input = Entry(width=51)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "huzaifa.khan.hz@gmail.com")
pass_input = Entry(width=33)
pass_input.grid(column=1, row=3)

search_button = Button(text="Search", width=15, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)
gen_button = Button(text="Generate Password", highlightthickness=0, command=generate_pass)
gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, highlightthickness=0, command=add_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
