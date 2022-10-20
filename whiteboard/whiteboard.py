from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

#icon
image_icon= PhotoImage(file="")
root.iconphoto(False,image_icon)

color_box=PhotoImage(file="")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)


root.mainloop()