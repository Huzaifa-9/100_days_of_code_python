from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles To Kilometer Converter")
# window.minsize(width=100, height=150)
window.config(padx=30,pady=30)

#Entries
entry = Entry(width=20)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=2, row=1)


#Buttons
def action():
    miles = float(entry.get())
    kilometer = round(1.609 * miles, 4)

    cl_label.config(text=kilometer)


#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)

#Labels
label = Label(text="Miles")
label.grid(column=3, row=1)

#Label KM
eq_label = Label(text="is equal to")
eq_label.grid(column=1, row=2)

cl_label = Label(text="0")
cl_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

window.mainloop()
