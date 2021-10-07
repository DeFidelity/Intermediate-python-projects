from tkinter import *

window = Tk()
window.title("angela first gui program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)


# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "some new text"
# or
my_label.config(text="label")
my_label.grid(column=0, row=0)
# any input value n the kwarg can easily be change as we would have change dictionary value.
# new button\
button2 = Button(text="don't click me")
button2.grid(column=2, row=0)
# Button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry, this is basically input in gui
my_input = Entry()
my_input.grid(column=3, row=3)

window.mainloop()
