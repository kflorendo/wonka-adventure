import Tkinter as tk     # python 2
from Tkinter import *
from PIL import ImageTk,Image
import os

output_text = ''
canvas = ''
enter_btn = ''
user_entry = ''
room_img = ''
title_text = ''
error_text = ''
#root.configure(background='black')

class WonkaApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        initializeGameRoom('inventroom.png','hi',self.frame)
        enter()
        runCandyShopRoom()

def runCandyShopRoom():
    
    displayTitle('Candy Shop')
    displayRoomImage('finalroom.png')
    display('Hello Charlie! \n\n1 = \'Hello!\' \n\nType \'1\' below and click \'ENTER\' to proceed.')
    get_r('1')
    display('The eccentric chocolatier Willy Wonka, who retired last year, just announced that there would be one final mission in his chocolate factory. \n\nClick \'ENTER\' to proceed.')
    enter()
    display('The person who finds the remaining 5 golden tickets wins an grand, mysterious prize. It\'s on the news everywhere!')
    enter()
    display('In order to get in to the factory, you must find the first golden ticket hidden in a candy store. Do you agree? \n\n1 = \'Okay!\'')
    get_r('1')
    display('Rumor has it the last golden ticket is at the candy store on your street... Would you like to visit? \n\ny = yes \nn = no')
    r = get_r('yn')
    if r == 'n':
        display('Your Grandpa Joe has been wanting to visit the candy store for a while. He forces you to go to the candy shop with him.')
        enter()
    elif r == 'y':
        display('You go together to the candy shop with Grandpa Joe who has been wanting to visit the candy store for a while.')
        enter()
    display('Along the way, you find 50 cents in the snow. Do you want to pick it up?\n\ny = yes \nn = no')
    r = get_r('yn')
    if r = 'n':

def initializeGameRoom(img,displaytext,root):
    global output_text
    global canvas
    global enter_btn
    global user_entry
    global room_img
    global title_text
    global error_text
    screenwidth = 700
    screenheight = 900
    screenbg = 'black'
    canvas = Canvas(root, bg = screenbg, width = screenwidth, height = screenheight)
    canvas.pack()
    #root = Tk()
    #root.geometry('800x800+0+0')
    title_text = canvas.create_text((screenwidth/2,30), anchor = N, fill = 'white', font =('Courier',14),text='Room')    
    
    imgpath = Image.open(os.path.dirname(os.path.abspath(__file__)) + '//' + img)
    resizedimg = imgpath.resize((500,500))
    screenroom_img = ImageTk.PhotoImage(resizedimg)
    displayimg = Label(image = screenroom_img)
    displayimg.image = screenroom_img
    room_img = canvas.create_window(screenwidth/2,75,window = displayimg, anchor = N)

    output_text = canvas.create_text((screenwidth/2,screenheight-300), anchor = N, fill = 'white', font =('Courier',12),text=displaytext, width = 525)
    error_text = canvas.create_text((screenwidth/2,screenheight-100), anchor = N, fill = 'red', font =('Courier',12),text='')
    
    user_entry = Entry(canvas, relief = FLAT, bd = 10)
    user_entry.config(font=("Courier", 14))
    user_entry.pack()
    canvas.create_window(screenwidth/2-50,screenheight-25,window = user_entry, anchor = S)

    enter_btn = Button(canvas, text = "ENTER", font = ('Courier',14),command = buttonInitialize())
    enter_btn.configure(bd = 5)
    enter_btn.pack()
    canvas.create_window(screenwidth/2+125,screenheight-25,window = enter_btn, anchor = S)
    canvas.update()

#functions for room:

def displayTitle(roomname):
    global title_text
    global canvas
    canvas.itemconfig(title_text,text=roomname)
    canvas.update()

def displayRoomImage(img):
    global room_img
    global canvas
    imgpath = Image.open(os.path.dirname(os.path.abspath(__file__)) + '//' + img)
    resizedimg = imgpath.resize((500,500))
    screenroom_img = ImageTk.PhotoImage(resizedimg)
    displayimg = Label(image = screenroom_img)
    displayimg.image = screenroom_img
    canvas.itemconfig(room_img,window=displayimg)
    canvas.update()
    
def enter(tk.event):             #use to wait for Enter btn, no text input
    global user_entry
    global canvas
    user_entry.configure(state='disabled')
    waitUntilButtonClicked()

def get_r(accepted_r):
    user_r = inputEnter().lower()
    while (user_r == '' or (user_r not in accepted_r)):
        canvas.itemconfig(error_text,text='Please enter valid input')
        canvas.update()
        user_r = inputEnter()
    canvas.itemconfig(error_text,text='')
    return user_r
    
def inputEnter():           #use to read text input
    global user_entry
    global canvas
    user_entry.configure(state='normal')
    user_entry.delete(0,'end')
    user_entry.focus()
    canvas.update()
    waitUntilButtonClicked()
    entered_text = readEntry()
    return entered_text

def display(displaytext):
    global output_text
    global canvas
    canvas.itemconfig(output_text,text=displaytext)
    canvas.update()


#helper functions:

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

def buttonInitialize():
    print 'button initialized'
    
def main():
    root = tk.Tk()
    app = WonkaApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
