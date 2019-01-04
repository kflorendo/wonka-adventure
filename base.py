import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import *
from tkinter.ttk import *

import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
from tkinter import ttk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('800x800+0+0')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Room1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Loading screen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        self.button = tk.Button(self,text="start", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=100, mode="determinate")
        self.progress.pack()
        
    def start(self):
        import time
        self.progress.start(2)
        for i in range(0,101,2):
            time.sleep(0.05)
            self.progress['value']=i
            self.progress.update()
        self.progress.stop()
        self.controller.show_frame("Room1")


class Room1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Charlie's House", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        path = "student.jpg"
        im = Image.open(path)
        ph = ImageTk.PhotoImage(im)
        label = tk.Label(Room1, image=ph)
        label.pack(side = "bottom", fill = "both", expand = "yes")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
'''
class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create new window", 
                                command=self.create_window)
        self.button.pack(side="top")

    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
    
    def bar():
        progress=Progressbar(tk,orient=VERTICAL,length=100,mode='determinate')
        import time
        progress.start(2)
        for i in range(0,101,2):
            time.sleep(0.1)
            progress['value']=i
            progress.update()
        progress.stop()
        progress.pack()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
    
Button(tk,text='foo',command=bar).pack()
mainloop()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
label.pack(side = "bottom", fill = "both", expand = "yes")

path = "chocolate.png"
im = Image.open(path)
ph = ImageTk.PhotoImage(im)
label2 = tk.Label(window, image=ph)
label2.pack(side = "bottom", fill = "both", expand = "yes")
label2.image=ph
#Start the GUI
window.mainloop()'''