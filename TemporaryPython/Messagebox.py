from tkinter import *
from tkinter import messagebox

window = Tk()
# Starting Configuration
blankicon = PhotoImage(width=1, height=1)
window.title("fr a virus")
window.iconphoto(False, blankicon)

# Command
def Click():
    messagebox.askokcancel(title="Hi", message="aa")

# Widget
button = Button(window, text="MessageBox")
button.config(command=Click)
button.pack()

window.mainloop()