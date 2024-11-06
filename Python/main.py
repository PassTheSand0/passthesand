import random
from tkinter import *

# Starting
window = Tk()
window.geometry("800x500")
window.title("PassTheSand")
window.config(background="#000000")
# Table
random_quote = []

# function
count = 0
def click():
    global count
    count += 1
    print(count)
    label_count.config(text=count)
    button.config(state=ACTIVE)

def typewriter(text, label, delay=30):
    label.config(text='wait')
    for i in range(len(text) + 1):
        window.after(i * delay, lambda i=i: label.config(text=text[:i]))
        
def submit():
    textinputed = entry.get()
    typewriter(textinputed, label)

def random_quote():
    random.shuffle

# button
button = Button(window, text="INCREASE THE NUMBER")
button.place(x=600, y=100)
button.config(command=click)
button.config(font=('System', 10))
button.config(bg='#000000')
button.config(fg='#ffffff')
button.config(activebackground='#1c1c1c')
button.config(activeforeground='#ffffff')

submit_button = Button(window, text="Submit", command=submit)
submit_button.place(x=708, y=175)
submit_button.config(font=('System'))
submit_button.config(bg='#000000')
submit_button.config(fg='#ffffff')

random_button = Button(window, text="Say A random phrase")
random_button.config(command=random_quote)

# User Input
entry = Entry()
entry.place(x=600, y=150)
entry.config(font=('System', 10))
entry.config(bg='#000000')
entry.config(fg='#ffffff')


# Widget
photo = PhotoImage(file='Python\\pass.png')
label = Label(window, font=('System', 40), background="#000000", fg='white', image=photo, compound="bottom")
label.place(x=0, y=0)

typewriter(text="PassTheSand", label=label)

label_count = Label(window, text=count, font=('System', 20), bg="#000000", fg="#ffffff")
label_count.place(x=600, y=50)


window.mainloop()