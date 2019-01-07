import Tkinter as Tk     # python 2
  
from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 800, height = 800)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.resize((700,700),Image.open("inventroom.png")))  
canvas.create_image(100, 20, anchor = NW, image=img)  

user_input = Entry(root, bd =5)
user_input.pack(side = RIGHT)
user_input.focus_set()

root.mainloop()
