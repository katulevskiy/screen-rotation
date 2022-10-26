import rotatescreen
from tkinter import *
from tkinter import ttk
import os

screen = rotatescreen.get_primary_display()
start_orientation = screen.current_orientation
screen.rotate_to(180)

#setup
win= Tk()
win.geometry("750x250")
path = os.path.join(os.path.dirname(__file__),"notpassword.txt")
with open(path, "r") as f:
    notpassword=f.readlines()[0]

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)
   
def checkpass(userinput):
    if userinput == notpassword:
        print("Hell yeah!")
        screen.rotate_to(0)
        
    else:
        print("GFY")
    
    win.destroy()
    input()

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()
userinput = entry.get()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command=checkpass(userinput)).pack(pady=20)





win.mainloop()


        






