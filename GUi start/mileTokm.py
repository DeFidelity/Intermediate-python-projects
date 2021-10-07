from tkinter import *


def calculator():
    inp = int(entry.get())
    km = inp * 1.689
    my_label.config(text=round(km))


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=400, height=400)
window.config(padx=30, pady=30)

entry = Entry()
entry.grid(column=1, row=0)

entry_label = Label(text="Miles")
entry_label.grid(column=2, row=0)


my_label3 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label3.grid(column=0, row=1)

my_label = Label(text="0", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

my_label2 = Label(text="km", font=("Arial", 24, "bold"))
my_label2.grid(column=2, row=1)

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)


window.mainloop()