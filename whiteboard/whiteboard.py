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
image_icon= PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

color_box=PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root, image=eraser, bg="#f2f3f5").place(x=30,y=400)

colors=Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, 'Button-1', lambda x: show_color('black'))
display_pallete()

canvas= Canvas(root,width=930,height=500,background="#fff",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>')
canvas.bind('<B1-Motion>')







root.mainloop()