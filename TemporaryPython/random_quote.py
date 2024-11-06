import random
from tkinter import *

# Starting Point
window = Tk()
icon = PhotoImage(file="Python\\dusttrust.png")
window.title("hi it me dusttrust")
window.iconphoto(True, icon)
window.geometry("800x500")
window.config(background="#000000")


# Tables
random_quote = [
    "Both of us are here,& standing alone in a broken world.",
    "i'll make sure i'll be the one to finish the job.",
    "3 Strike and your OUT!"
]

# Functions
def typewriter(text, label, delay=40):
    label.config(text="")
    for i in range(len(text) + 1):
        window.after(i * delay, lambda i=i: label.config(text=text[:i]))
        
def random_quote_function():
    quote = random.choice(random_quote)
    typewriter(text=quote, label=label)

# Widgets
button = Button(window, text="Press Me")
button.pack()
button.config(bg="#000000")
button.config(fg="#ffffff")
button.config(font="Sans")
button.config(command=random_quote_function)

label = Label(window)
label.place(x=400, y=230, anchor=CENTER)
label.config(font="Sans")
label.config(bg="#000000")
label.config(fg="#ffffff")


window.mainloop()