from tkinter import *

# Starting Config
window = Tk()
window.title("Frames")
blankicon = PhotoImage(width=1, height=1)
window.iconphoto(False, blankicon)

# Variable
windowmove = 65
allmoveable_window = []

# Function
def launched():
    global moveable_window
    moveable_window = Toplevel(window)
    moveable_window.iconphoto(False, blankicon)
    moveable_window.geometry(f"100x100+{500}+{500}")
    allmoveable_window.append(moveable_window)
    launch_button.config(state=ACTIVE)

def window_move_up():
    global moveable_window
    if moveable_window is None:
        return
    
    current_geom = moveable_window.geometry().split('+')
    
  
    current_x = int(current_geom[1])
    current_y = int(current_geom[2])
    
   
    new_y = current_y - windowmove 
    moveable_window.geometry(f"100x100+{current_x}+{new_y}")
def window_move_down():
    global moveable_window
    if moveable_window is None:
        return
    
    current_geom = moveable_window.geometry().split('+')
    
  
    current_x = int(current_geom[1])
    current_y = int(current_geom[2])
    
   
    new_y = current_y + windowmove
    moveable_window.geometry(f"100x100+{current_x}+{new_y}")
def window_move_left():
    global moveable_window
    if moveable_window is None:
        return
    
    current_geom = moveable_window.geometry().split('+')
    
  
    current_x = int(current_geom[1])
    current_y = int(current_geom[2])
    
   
    new_x = current_x - windowmove
    moveable_window.geometry(f"100x100+{new_x}+{current_y}")
def window_move_right():
    global moveable_window
    if moveable_window is None:
        return
    
    current_geom = moveable_window.geometry().split('+')
    
  
    current_x = int(current_geom[1])
    current_y = int(current_geom[2])
    
   
    new_x = current_x + windowmove
    moveable_window.geometry(f"100x100+{new_x}+{current_y}")
    
# Frames
frame = Frame(window, bg="black",bd=5)
frame.pack()

# Widgets
W = Button(frame, text="W", font="Sans",width=3, command=window_move_up).pack(side=TOP)
A = Button(frame, text="A", font="Sans",width=3, command=window_move_left).pack(side=LEFT)
S = Button(frame, text="S", font="Sans",width=3, command=window_move_down).pack(side=LEFT)
D = Button(frame, text="D", font="Sans",width=3, command=window_move_right).pack(side=LEFT)

launch_button = Button(window, text="Create a New Window", font="Sans", command=launched)
launch_button.pack()

checkbutton = Checkbutton(window, text="Move all Window", font="Sans")
checkbutton.pack()

window.mainloop()