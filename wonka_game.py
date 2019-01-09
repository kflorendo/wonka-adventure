import tkinter as tk     # python 2
from tkinter import *  
from PIL import ImageTk,Image  

class room1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.newWindow = gameroom('inventroom.png','hi',self.master)
        '''self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('800x800+0+0')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)'''

def gameroom(img,displaytext,root):
    screenwidth = 800
    screenheight = 800
    screenbg = 'black'
    #root = Tk()
    #root.geometry('800x800+0+0')
    
    canvas = Canvas(root, bg = screenbg, width = screenwidth, height = screenheight) 
    #root.configure(background='black')
    canvas.pack()
    title_label = Label(canvas, text='INVENT ROOM', fg = 'white', bg = screenbg)
    title_label.config(font=("Courier", 14))
    title_label.pack()
    canvas.create_window(screenwidth/2,30,window = title_label, anchor = N) 
    
    room_img = Image.open(img)
    resizedimg = room_img.resize((500,500))
    screenroom_img = ImageTk.PhotoImage(resizedimg)  
    canvas.create_image(screenwidth/2, 75, anchor = N, image=screenroom_img)  
    #label_img = Label(root,image=screenimg)
    #label_img.place(x=150,y=50)
    output_label = Label(canvas, text=displaytext, fg = 'white', bg = screenbg,wraplength=500)
    output_label.config(font=("Courier", 14))
    output_label.pack()
    canvas.create_window(screenwidth/2,screenheight-200,window = output_label, anchor = N)    
    
    user_entry = Entry(canvas, bd = 10)
    user_entry.config(font=("Courier", 14))
    canvas.create_window(screenwidth/2,screenheight-25,window = user_entry, anchor = S)
    canvas.update()
    
    #root.mainloop()

def main(): 
    root = tk.Tk()
    app = room1(root)
    root.mainloop()

if __name__ == '__main__':
    main()