import Tkinter as tk     # python 2
from Tkinter import *
from PIL import ImageTk,Image
import os

output_text = ''
canvas = ''
enter_btn = ''
user_entry = ''
#root.configure(background='black')

class room1:
    global output_text
    global canvas
    global enter_btn
    global user_entry
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        output_text = ''
        canvas = ''
        enter_btn = ''
        user_entry = ''
        gameroom('inventroom.png','hi',self.frame)
        waitEnter()
        display('hey')
        print inputEnter()

def gameroom(img,displaytext,root):
    global output_text
    global canvas
    global enter_btn
    global user_entry
    screenwidth = 800
    screenheight = 800
    screenbg = 'black'
    canvas = Canvas(root, bg = screenbg, width = screenwidth, height = screenheight)
    canvas.pack()
    #root = Tk()
    #root.geometry('800x800+0+0')
    title_label = Label(canvas, text='INVENT ROOM', fg = 'white', bg = screenbg)
    title_label.config(font=("Courier", 14))
    title_label.pack()
    canvas.create_window(screenwidth/2,30,window = title_label, anchor = N)

    room_img = Image.open(os.path.dirname(os.path.abspath(__file__)) + '//' + img)
    resizedimg = room_img.resize((500,500))
    screenroom_img = ImageTk.PhotoImage(resizedimg)
    displayimg = Label(image = screenroom_img)
    displayimg.image = screenroom_img
    canvas.create_window(screenwidth/2,75,window = displayimg, anchor = N)
    '''self.screenroom_img = screenroom_img
    canvas.create_image(screenwidth/2, 75, anchor = N, image=screenroom_img)'''

    #label_img = Label(root,image=screenimg)
    #label_img.place(x=150,y=50)
    '''output_label = Label(canvas, text=displaytext, fg = 'white', bg = screenbg,wraplength=500)
    output_label.config(font=("Courier", 14))
    output_label.pack()'''
    output_text = canvas.create_text((screenwidth/2,screenheight-200), anchor = N, fill = 'white', font =('Courier',14),text=displaytext)
    #canvas.create_window(screenwidth/2,screenheight-200,window = output_label, anchor = N)
    #output_text = canvas.create_window(screenwidth/2,screenheight-200,window = output_label, anchor = N)

    user_entry = Entry(canvas, relief = FLAT, bd = 10)
    user_entry.config(font=("Courier", 14))
    user_entry.pack()
    canvas.create_window(screenwidth/2-50,screenheight-25,window = user_entry, anchor = S)

    enter_btn = Button(canvas, text = "ENTER", font = ('Courier',14),command = enter())
    enter_btn.configure(bd = 5)
    enter_btn.pack()
    canvas.create_window(screenwidth/2+125,screenheight-25,window = enter_btn, anchor = S)
    canvas.update()
    #root.mainloop()

def waitEnter():             #use to wait for Enter btn, no text input
    global user_entry
    global canvas
    user_entry.configure(state='disabled')
    waitUntilButtonClicked()

def inputEnter():           #use to read text input
    global user_entry
    global canvas
    user_entry.configure(state='normal')
    user_entry.delete(0,'end')
    user_entry.insert(0,'typehere')
    canvas.update()
    waitUntilButtonClicked()
    entered_text = readEntry()
    return entered_text

def readEntry():
    global user_entry
    user_entered = user_entry.get()
    user_entry.delete(0,'end')
    canvas.update()
    return user_entered

def waitUntilButtonClicked():
    global enter_btn
    global canvas
    var = tk.IntVar()
    enter_btn.configure(command=lambda: var.set(1))
    canvas.update()
    enter_btn.wait_variable(var)
    print 'button clicked'

def enter():
    print "hey"

def display(displaytext):
    global output_text
    global canvas
    canvas.itemconfig(output_text,text=displaytext)
    canvas.update()

def main():
    root = tk.Tk()
    app = room1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
