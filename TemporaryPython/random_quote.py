import random
from tkinter import *

# Starting Point
window = Tk()
window.title("app")
window.geometry("800x500")
window.config(background="#000000")


# Tables
random_quote = [
    "Ayam",
    "Nasi Lemak",
    "oaa"
]

# Functions
def typewriter(text, label, delay=40):
    label.config(text="")
    for i in range(len(text) + 1):
        window.after(i * delay, lambda i=i: label.config(text=text[:i]))
        
def typewriter_fast(text, label, delay=20):
    label.config(text="")
    for i in range(len(text) + 1):
        window.after(i * delay, lambda i=i: label.config(text=text[:i]))
    
def random_quote_function():
    quote = random.choice(random_quote)
    typewriter(text=quote, label=label)

# Widgets
button = Button(window, text="Press")
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