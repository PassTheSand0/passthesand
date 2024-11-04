from tkinter import *

# Starting
window = Tk()
window.geometry("800x500")
window.title("Dusttrust")

# Configuration
window.config(background="#000000")

# function
count = 0
def Click():
    global count
    count += 1
    print(count)
    label_count.config(text=count)
    button.config(state=ACTIVE)

# button
button = Button(window, text="About Me")
button.place(x=600, y=100)
button.config(command=Click)
button.config(font=('System', 10))
button.config(bg='#000000')
button.config(fg='#ffffff')
button.config(activebackground='#1c1c1c')
button.config(activeforeground='#ffffff')


# Widget
photo = PhotoImage(file='Python\\pass.png')
label = Label(window,text="PassTheSand", font=('System', 40), background="#000000", fg='white', image=photo, compound="bottom")
label.place(x=0, y=0)

label_count = Label(window, text=count, font=('System', 20), bg="#000000", fg="#ffffff")
label_count.place(x=600, y=50)



window.mainloop()