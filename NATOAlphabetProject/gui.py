from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

#Labels
my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

#Buttons
#calls action() when pressed
button = Button(text="New Button")
button.grid(column=3, row=1)


def action():
    print("Do something")


#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=2, row=2)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=4, row=4)

window.mainloop()
