import tkinter
from tkinter import *

window = Tk()
window.title("My GUI")
window.minsize(width=300, height=200)
my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)
new_label = tkinter.Label(text="Miles")
new_label.grid(column=3, row=0)
news_label = tkinter.Label(text="Km")
news_label.grid(column=3, row=1)


def clicked():
    new_input = float(inputs.get())
    result = round(1.609 * new_input)
    latest.config(text=f"{result}")


button = tkinter.Button(text="Calculate", command=clicked)
button.grid(column=2, row=5)
inputs = tkinter.Entry()
inputs.grid(column=2, row=0)
latest = tkinter.Label(text="0")
latest.grid(column=2, row=1)

window.mainloop()
