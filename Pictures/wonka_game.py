import Tkinter as tk     # python 2
from Tkinter import *
from PIL import ImageTk,Image
import os
import random

output_text = ''
canvas = ''
enter_btn = ''
user_entry = ''
room_img = ''
title_text = ''
error_text = ''
entVar = ''
backpack_btn = ''
backpack_frame = ''
backpack_text = ''
money = 0
bag = ['0.00']
masterRoot = ''
chocolateFail = False
candyShopSuccess = False
chocolateRoomSuccess = False
startBtn = ''
screenroom_img = ''

#root.configure(background='black')

class WonkaApp:
    def __init__(self, master):
        global masterRoot
        global startBtn
        masterRoot = master
        self.master = master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
        self.master.configure(background="black")

        mainframe = tk.Frame(masterRoot,bg="black")
        mainframe.pack()
        #mainframe.place(anchor = 'n',x=(master.winfo_screenwidth()-pad)/2,y=500)
        startLbl = Label(mainframe,bg="black",fg="white",text="Willy Wonka Game",font=("Courier",48))
        startLbl.pack()

        var = tk.IntVar()
        startBtn = Button(mainframe, text = "START GAME", font = ('Courier',14),command =lambda: var.set(1))
        startBtn.pack()

        startBtn.wait_variable(var)
        startBtn.destroy()
        startLbl.destroy()
        self.initializeGameRoom('finalroom.png',' ',mainframe)
        #run room functions:
        runCandyShopRoomIntro()
        display('Oh no! Turns out Willy Wonka has trapped you inside his factory. You must succeed and get the golden ticket in each room to enter the final room.')
        enter()
        display('Maybe you\'ll see him in the final room....')
        enter()
        runHomeScreen()

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


    def initializeGameRoom(self,img,displaytext,root):
        global output_text
        global canvas
        global enter_btn
        global user_entry
        global room_img
        global title_text
        global error_text
        global backpack_btn
        global backpack_frame
        global backpack_text
        global masterRoot
        global screenroom_img
        screenwidth = 1900
        screenheight = 1120
        screenbg = 'black'
        canvas = Canvas(root, bg = screenbg, width = screenwidth, height = screenheight)
        canvas.pack()
        #root = Tk()
        #root.geometry('800x800+0+0')
        title_text = canvas.create_text((600,50), anchor = N, fill = 'white', font =('Courier',14),text='Room')

        imgpath = Image.open(os.path.dirname(os.path.abspath(__file__)) + '//' + img)
        resizedimg = imgpath.resize((500,500))
        screenroom_img = ImageTk.PhotoImage(resizedimg)
        room_img = canvas.create_image((600,100),image = screenroom_img,anchor = 'n')
        canvas.update()

        output_text = canvas.create_text((600,660), anchor = N, fill = 'white', font =('Courier',14),text=displaytext, width = 500)
        error_text = canvas.create_text((600,screenheight-275), anchor = N, fill = 'red', font =('Courier',12),text='')
        canvas.create_line(1200,0,1200,1800, fill="white")

        user_entry = Entry(canvas, relief = FLAT, bd = 10)
        user_entry.config(font=("Courier", 14))
        user_entry.pack()
        canvas.create_window(600-100,screenheight-200,window = user_entry, anchor = S)

        enter_btn = Button(canvas, text = "ENTER", font = ('Courier',14),command = retFunc)
        enter_btn.configure(bd = 5)
        enter_btn.pack()
        canvas.create_window(600+100,screenheight-200,window = enter_btn, anchor = S)
        masterRoot.bind('<Return>',retFunc)

        backpack_frame = tk.Frame(masterRoot,width=500,height=750,bg="black")
        backpack_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
        backpack_text = Label(backpack_frame,bg="black",fg="white",text="test",font=("Courier",12))
        backpack_text.pack()
        backpack_frame.place(anchor = N,x=1550, y=250)

        #backpack_text = canvas.create_text((screenwidth/2,screenheight-300), anchor = N, fill = 'white', font =('Courier',14),text=displaytext, width = 500)
        backpack_btn = Button(canvas, text = "Open Backpack", font = ('Courier',12),command = displayBackpack)
        backpack_btn.configure(bd = 5)
        backpack_btn.pack()
        canvas.create_window(1550,200,window = backpack_btn, anchor = N)
        canvas.update()
        root.lift()

def displayBackpack():
    global bag
    global backpack_btn
    global canvas
    global backpack_frame
    global backpack_text
    global masterRoot
    displayBackpackString = 'Backpack:\n'
    for item in bag:
        displayBackpackString += str(item) + '\n'
    backpack_text.config(text = displayBackpackString)
    backpack_frame.lift()
    enter_btn.configure(state="disabled")
    masterRoot.unbind('<Return>')
    backpack_btn.configure(text = 'Close Backpack',command = closeBackpack)
    canvas.update()

def closeBackpack():
    global backpack_btn
    global canvas
    global backpack_frame
    global masterRoot
    backpack_frame.lower()
    backpack_btn.configure(text = 'Open Backpack',command = displayBackpack)
    enter_btn.configure(state="normal")
    masterRoot.bind('<Return>',retFunc)
    canvas.update()

#room functions:

def runHomeScreen():
    global candyShopSuccess
    displayRoomImage('lobby_without_finalroom.png')
    gameRunning = True
    lives = 5
    chocolateRoomSuccess = False
    inventRoomSuccess = False
    squirrelRoomSuccess = False
    tvRoomSuccess = False
    finalRoom = False
    while(gameRunning):
        display('What room do you want to enter?\n\n1 = Candy Shop\n2 = Chocolate Room\n3 = Inventing Room\n4 = Squirrel Room\n5 = TV Room')
        r = get_r('12345')
        if r == '1':
            if candyShopSuccess == True:
                display('You\'ve already completed this room. Try entering a different room.')
                enter()
            elif candyShopSuccess == False:
                roomSuccess = runCandyShopRoom()
                if roomSuccess == 'fail':
                    lives-=1
                    display('You lost a life. You have '+ str(lives) + ' remaining.')
                    enter()
        elif r == '2':
            if chocolateRoomSuccess == True:
                display('You\'ve already completed this room. Try entering a different room.')
                enter()
            elif chocolateRoomSuccess == False:
                roomSuccess = runChocolateRoom()
                if roomSuccess == 'fail':
                    lives-=1
                    display('You lost a life. You have '+ str(lives) + ' remaining.')
                    enter()
                elif roomSuccess == 'success':
                    chocolateRoomSuccess = True
        elif r == '3':
            if inventRoomSuccess == True:
                display('You\'ve already completed this room. Try entering a different room.')
                enter()
            elif inventRoomSuccess == False:
                roomSuccess = runInventRoom()
                if roomSuccess == 'fail':
                    lives-=1
                    display('You lost a life. You have '+ str(lives) + ' remaining.')
                    enter()
                elif roomSuccess == 'success':
                    inventRoomSuccess = True
        elif r == '4':
            if squirrelRoomSuccess == True:
                display('You\'ve already completed this room. Try entering a different room.')
                enter()
            elif squirrelRoomSuccess == False:
                roomSuccess = runSquirrelRoom()
                if roomSuccess == 'fail':
                    lives-=1
                    display('You lost a life. You have '+ str(lives) + ' remaining.')
                    enter()
                elif roomSuccess == 'success':
                    squirrelRoomSuccess = True
        elif r == '5':
            if tvRoomSuccess == True:
                display('You\'ve already completed this room. Try entering a different room.')
                enter()
            elif tvRoomSuccess == False:
                roomSuccess = runTVRoom()
                if roomSuccess == 'fail':
                    lives-=1
                    display('You lost a life. You have '+ str(lives) + ' remaining.')
                    enter()
                elif roomSuccess == 'success':
                    tvRoomSuccess = True
        if ('Golden Ticket 1' in bag) and ('Golden Ticket 2' in bag) and ('Golden Ticket 3' in bag) and ('Golden Ticket 4' in bag) and ('Golden Ticket 5' in bag):
            gameRunning = False
            finalRoom = True

        #check if player lost all 5 lives, then exit game
        if lives <= 0:
            display('You died! Thanks for playing :)')
            gameRunning = False
            enter()
            return 'end'

    if(finalRoom == True):
            display('Congratulations! You can now enter the final room.')
            enter()
            displayRoomImage('lobby_with_finalroom.png')
            gameRunning = False
            while(gameRunning):
                display('What room do you want to enter?\n\n1 = Candy Shop\n2 = Chocolate Room\n3 = Inventing Room\n4 = Squirrel Room\n5 = TV Room\n6 = Final Room')
                r = get_r('123456')
                if r == '1':
                    if candyShopSuccess == True:
                        display('You\'ve already completed this room. Try entering a different room.')
                        enter()
                    elif candyShopSuccess == False:
                        roomSuccess = runCandyShopRoom()
                        if roomSuccess == 'fail':
                            lives-=1
                            display('You lost a life. You have '+ str(lives) + ' remaining.')
                            enter()
                elif r == '2':
                    if chocolateRoomSuccess == True:
                        display('You\'ve already completed this room. Try entering a different room.')
                        enter()
                    elif chocolateRoomSuccess == False:
                        roomSuccess = runChocolateRoom()
                        if roomSuccess == 'fail':
                            lives-=1
                            display('You lost a life. You have '+ str(lives) + ' remaining.')
                            enter()
                        elif roomSuccess == 'success':
                            chocolateRoomSuccess = True
                elif r == '3':
                    if inventRoomSuccess == True:
                        display('You\'ve already completed this room. Try entering a different room.')
                        enter()
                    elif inventRoomSuccess == False:
                        roomSuccess = runInventRoom()
                        if roomSuccess == 'fail':
                            lives-=1
                            display('You lost a life. You have '+ str(lives) + ' remaining.')
                            enter()
                        elif roomSuccess == 'success':
                            inventRoomSuccess = True
                elif r == '4':
                    if squirrelRoomSuccess == True:
                        display('You\'ve already completed this room. Try entering a different room.')
                        enter()
                    elif squirrelRoomSuccess == False:
                        roomSuccess = runSquirrelRoom()
                        if roomSuccess == 'fail':
                            lives-=1
                            display('You lost a life. You have '+ str(lives) + ' remaining.')
                            enter()
                        elif roomSuccess == 'success':
                            squirrelRoomSuccess = True
                elif r == '5':
                    if tvRoomSuccess == True:
                        display('You\'ve already completed this room. Try entering a different room.')
                        enter()
                    elif tvRoomSuccess == False:
                        roomSuccess = runTVRoom()
                        if roomSuccess == 'fail':
                            lives-=1
                            display('You lost a life. You have '+ str(lives) + ' remaining.')
                            enter()
                        elif roomSuccess == 'success':
                            tvRoomSuccess = True
                elif r == '6':
                    result = runFinalRoom()
                    if result == 'fail':
                        lives-=1
                        display('You lost a life. You have '+ str(lives) + ' remaining.')
                        enter()
                    elif result == 'success':
                        return 'end'
                #check if player lost all 5 lives, then exit game
                if lives <= 0:
                    display('You died! Thanks for playing :)')
                    gameRunning = False
                    enter()
                    return 'end'


def runCandyShopRoomIntro():
    global money
    global candyShopSuccess
    displayTitle('Candy Shop')
    displayRoomImage('candyshop.png')
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
        display('Aw, man. Your Grandpa Joe has been wanting to visit the candy store for a while, so he forces you to go to the candy shop with him.')
        enter()
    else:
        display('You go together to the candy shop with Grandpa Joe who has been wanting to visit the candy store for a while.')
        enter()
    display('Along the way, you find 50 cents in the snow. Do you want to pick it up?\n\ny = yes \nn = no')
    r = get_r('yn')
    if r == 'y':
        money += .50
        display('You have gained 50 cents! Maybe you can get some more later. \n\nOpen your backpack to see your new money.')
        bag[0]=('%.2f'%money)
        enter()
    else:
        display('You have no money now. But at least you\'ve got a good conscience. Maybe Grandpa Joe can help you out later.')
        enter()
    display('You\'ve reached the candy shop!')
    enter()
    #NOTE: Change candy in the following line to items that we can actually use later on
    display('Candy Register Guy: "Hi, Charlie! Nice to see you again. I see you\'re with your Grandpa Joe..."')
    enter()
    room_unsolved = True
    while(room_unsolved):
        display('"What would you like today, Charlie?" \n\n1 = "I\'ll have some candy."\n2 = "Can you turn on the TV?"\n3 = "I don\'t know."')
        r = get_r('123')
        if r == '1':
            display(('Candy Register Guy: "What candy would you like?"\n\nYour balance: %.2f cents.\n\n1 = Laffy Taffy \t$0.10\n2 = Giant SweeTarts \t$0.10\n3 = Luminous Lollipop \t$0.15\n4 = Gobstoppers \t$0.25\nq = quit')%money)
            r = get_r('12345q')
            if r == '1':
                if money < 0.10:
                    display('You don\'t have enough money to buy the Laffy Taffy. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                        return 'fail'
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.10
                    bag.append('Laffy Taffy')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
            elif r == '2':
                if money < 0.10:
                    display('You don\'t have enough money to buy the SweeTarts. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                        return 'fail'
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.10
                    bag.append('SweeTarts')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
            elif r == '3':
                if money < 0.15:
                    display('You don\'t have enough money to buy the Lollipop. Candy Register Guy, being the kind man he is, offers it to you for free! Would you like to accept it? \n\ny = yes\nn = no')
                    r = get_r('yn')
                    if r == 'y':
                        display('Wow! Turns out it isn\'t just a normal lollipop. It lights up! It is put into your backpack. \n\nWho knows, it might be useful in the future....')
                        enter()
                    elif r == 'n':
                        display('Candy Register Guy: "Alright, Charlie. But you\'re missing out."')
                        enter()
                else:
                    display('You bought the candy! \nWow! Turns out it isn\'t just a normal lollipop. It\'s a Luminous Lollipop! It is put into your backpack. \n\nWho knows, it might be useful in the future....')
                    money -= 0.15
                    bag.append('Luminous Lollipop')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
                    candyShopSuccess = True
            elif r == '4':
                if money < 0.25:
                    display('You don\'t have enough money to buy the SweeTarts. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.25
                    bag.append('Gobstoppers')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
        elif r == '2':
            display('"Of course, Charlie! Here, I\'ll switch it on for you..."')
            enter()
            display('"Oh wait... what\'s that? Wonka\'s having another competition for golden tickets!"')
            enter()
            display('"That reminds me, I have one last Wonka Chocolate Bar." \nGrandpa Joe: "I remember Wonka! That man was a character." \n\n1 - Ask Grandpa Joe more about Wonka\n2 - Ask to see the chocolate bar')
            r = get_r('12')
            grandpasymp = False
            if r == '1':
                display('Grandpa Joe: "Oh, Charlie those were the most wonderful times. Wonka was such a polite soul with peculiar ideas for his chocolate factory. I enjoyed working there very much."')
                enter()
                display('Grandpa Joe seems to be getting pretty nostalgic...')
                enter()
                grandpasymp = True
            display('Candy Register Guy: "So, would you like the last Wonka Bar? Maybe you\'ll get the last golden ticket! It\'s only $0.60."\n\ny = yes\nn = no')
            r = get_r('yn')
            if r == 'y':
                display(('"Hmm... but you only have %.2f cents." \n\n1 - Ask Grandpa Joe to borrow money\n2 - Take the chocolate bar and run\n3 - Don\'t buy the chocolate bar') % money)
                r = get_r('123')
                if r == '1':
                    if grandpasymp == True:
                        display('Grandpa Joe: "Of course, Charlie! For old times sakes. Here, I\'ll pay for it."\n\nGrandpa Joe hands you the chocolate bar.')
                        enter()
                        display('You unwrap the chocolate bar and find the golden ticket! Congratulations! \n\nThe ticket has been added to your backpack.')
                        bag.append('Golden Ticket 1')
                        room_unsolved = False
                        enter()
                        return 'success'
                    else:
                        display('You ask Grandpa Joe for money, but he gets mad at you. There is no way he could spend that much money on a chocolate bar. You died. Return to start page.') #restart
                        enter()
                        return 'fail'
                elif r == '2':
                    display('You take it and run as fast as you can out the candy store door. Candy Register Guy calls the police and has you arrested.')
                    enter()
                    display('You died. Return to start page.') #restart
                    enter()
                    return 'fail'
                elif r == '3':
                    display('Candy Register Guy: "Alright, Charlie. Just know kids around the world want this chococlate bar!"') #return to asking
                    enter()
            elif r == 'n':
                display('Candy Register Guy: "Alright, Charlie. Just know kids around the world want this chococlate bar!"') #return to asking
                enter()
        elif r == '3':
            display('Candy Register Guy: "I can\'t help you there, old sport. I\'ll be here whenever you\'re ready."')
            enter()

def runCandyShopRoom():
    global money
    global candyShopSuccess
    room_unsolved = True
    displayTitle('Candy Shop Room')
    displayRoomImage('candyshop.png')
    while(room_unsolved):
        display('"What would you like today, Charlie?" \n\n1 = "I\'ll have some candy."\n2 = "Can you turn on the TV?"\n3 = "I don\'t know."\nq = return to home screen')
        r = get_r('123q')
        if r == '1':
            display(('Candy Register Guy: "What candy would you like?"\n\nYour balance: %.2f cents.\n\n1 = Laffy Taffy \t$0.10\n2 = Giant SweeTarts \t$0.10\n3 = Luminous Lollipop \t$0.15\n4 = Gobstoppers \t$0.25\nq = return to home screen')%money)
            r = get_r('12345q')
            if r == '1':
                if money < 0.10:
                    display('You don\'t have enough money to buy the Laffy Taffy. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                        return 'fail'
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.10
                    bag.append('Laffy Taffy')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
            elif r == '2':
                if money < 0.10:
                    display('You don\'t have enough money to buy the SweeTarts. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                        return 'fail'
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.10
                    bag.append('SweeTarts')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
            elif r == '3':
                if money < 0.15:
                    display('You don\'t have enough money to buy the Lollipop. Candy Register Guy, being the kind man he is, offers it to you for free! Would you like to accept it? \n\ny = yes\nn = no')
                    r = get_r('yn')
                    if r == 'y':
                        display('Wow! Turns out it isn\'t just a normal lollipop. It lights up! It is put into your backpack. \n\nWho knows, it might be useful in the future....')
                        enter()
                    elif r == 'n':
                        display('Candy Register Guy: "Alright, Charlie. But you\'re missing out."')
                        enter()
                else:
                    display('You bought the candy! \nWow! Turns out it isn\'t just a normal lollipop. It\'s a Luminous Lollipop! It is put into your backpack. \n\nWho knows, it might be useful in the future....')
                    money -= 0.15
                    bag.append('Luminous Lollipop')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
                    candyShopSuccess = True
                    room_unsolved = False
            elif r == '4':
                if money < 0.25:
                    display('You don\'t have enough money to buy the SweeTarts. What do you want to do? \n\n1 = Steal it\n2 = Ask Grandpa Joe for money')
                    r = get_r('12')
                    if r == '1':
                        display('You try to steal the candy bar... but you get caught! Oh no! You died. Return to start page.') #restart
                        enter()
                    elif r == '2':
                        display('You ask Grandpa Joe for money, but he gets mad at you. He does not give you the money. How do you have the nerve to use money for some useless candy?') #restart
                        enter()
                else:
                    display('You bought the candy! It is put into your backpack.') #item in backpack
                    money -= 0.25
                    bag.append('Gobstoppers')
                    if money > 0:
                        bag[0] = ('%.2f'%money)
                    else:
                        bag[0] = '0.00'
                    enter()
            elif r == 'q':
                return
        elif r == '2':
            display('"Of course, Charlie! Here, I\'ll switch it on for you..."')
            enter()
            display('"Oh look! It\'s Jeopardy, my favorite show!"')
            enter()
        elif r == '3':
            display('Candy Register Guy: "I can\'t help you there, old sport. I\'ll be here whenever you\'re ready."')
            enter()
        elif r == 'q':
            return

def runChocolateRoom():
    global money
    global chocolateFail
    goldenTicketFound = False
    room_unsolved = True
    displayTitle('Chocolate Room')
    displayRoomImage('chocolateroom2.png')
    if "Luminous Lollipop" in bag:
        health = 0
        display('Oh no! The room is dark and you can\'t see anything. Fortunately, you have the <LUMINOUS LOLLIPOP> in your backpack! Use it to light up the room.\n\n1 = use lollipop\nq = return to home')
        r = get_r('1q')
        if r == '1':
            displayRoomImage('chocolate.png')
            display('Now you can finally see! Turns out everything in the room is edible. Yum!')
            enter()
            display('You realize you\'re starving and could eat any of the things in the room. But, you have to make sure to be secretive about taking the food!')
            enter()
            display('If you eat too much, the Ooompa Loompas will know and come after you. Be careful!')
            enter()

            while (room_unsolved):
                display('Your Health: ' + str(health) + '\\100\nWhat would you like to eat? \n\n1 = Candy Apples\n2 = Chocolate Bark\n3 = Gumdrop Pebbles\n4 = Cotton Candy Clouds\n5 = Chocolate from the Chocolate River\n6 = Candy Shroom\n7 = Golden Leaf\nq = return to home')
                r = get_r('1234567q')
                if r == '1':
                    health += 60
                    display('Yum! That candy apple was delicious! \n+60 to your health.\n\nYour Health: ' + str(health) + '\\100')
                    enter()
                elif r == '2':
                    health += 30
                    display('Mmmm... the chocolate bark was really satisfying. \n+30 to your health. \n\nYour Health: ' + str(health) + '\\100')
                    enter()
                elif r == '3':
                    health += 70
                    display('Delicious! Those gumdrop pebbles taste really realistic... \n+70 to your health. \n\nYour Health: ' + str(health) + '\\100')
                    enter()
                elif r == '4':
                    health += 15
                    display('That was a cloud of deliciousness! \n+15 to your health. \n\nYour Health: ' + str(health) + '\\100')
                    enter()
                elif r == '5':
                    display('You go to get a handful of chocolate from the chocolate river. But oh no! \nYou fall in to the river!')
                    enter()
                    display('You lost a life. Return to home screen.')
                    enter()
                    return 'fail'
                elif r == '6':
                    health -= 10
                    display('You eat the mushroom, but it tastes a little funky. You don\'t feel so good.\n-10 to your health. \n\nYour health: ' + str(health) + '\\100')
                    enter()
                elif r == '7':
                    display('You go to eat the golden leaf, but it looks a little strange. There\'s a wrapper on the outside! Would you like to unwrap it?\n\ny = yes\nn = no')
                    r = get_r('yn')
                    if r == 'y':
                        display('You unwrap the golden leaf and inside is a golden ticket! Congratulations! \n\nThe ticket has been added to your backpack.')
                        bag.append('Golden Ticket 2')
                        enter()
                        display('But make sure to refill your hunger levels, or you won\'t be able to keep the ticket!')
                        enter()
                        goldenTicketFound = True
                elif r == 'q':
                    return
                if health == 100:
                    display('Your health: ' + str(health) + '\\100 \n\nYum, you filled up your hunger levels successfully without the Oompa Loompas catching you!')
                    enter()
                    if goldenTicketFound == True:
                        display('Congratulations! You beat the room and you can keep your golden ticket.')
                        enter()
                        room_unsolved = False
                        return 'success'
                    elif goldenTicketFound == False:
                        display('But there still might be something important in this room... maybe you can come back and find it next time.')
                        enter()
                        return
                elif health > 100:
                    display('Your health: ' + str(health) + '\\100 \n\nOh no! The Oompa Loompas noticed you\'re taking too much candy from the room and captured you.')
                    enter()
                    display('You died. Better luck next time.')
                    enter()
                    if 'Golden Ticket 2' in bag:
                        bag.remove('Golden Ticket 2')
                    return 'fail'
                elif health < 0:
                    display('Your health: ' + str(health) + '\\100 \n\nYou\'re health dropped too low!')
                    enter()
                    display('You died. Better luck next time.')
                    enter()
                    if 'Golden Ticket 2' in bag:
                        bag.remove('Golden Ticket 2')
                    return 'fail'
        elif r == 'q':
            return 'fail'
    elif ("Luminous Lollipop" not in bag) and (chocolateFail == False):
        display('Oh no! The room is dark and you can\'t see anything. \n\nIt seems like you\'ll need something to light up the room...')
        enter()
        display('Maybe you can go visit a different room and see if you can find anything. Here\'s 0.50 cents to help you out!\n\nItem added to backpack.')
        money += 0.50
        bag[0] = ('%.2f'%money)
        chocolateFail == True
        enter()
        return
    elif chocolateFail == True:
        display('The room is still dark! You can\'t see anything unless you find something to light up the room. Maybe go back to where it all started...?')
        enter()
        return

#Invent room function
def runInventRoom():
    global bag
    displayTitle('Inventing Room')
    displayRoomImage('inventroom.png')
    cabinet_contents = ["secret formula", "deflation gumdrops"]
    
    candy_recipe_folder = ["fruity tooty lollipop recipe","groovy grape taffy recipe","twisty tangy twizzlers recipe"]
    chocolate_recipe_folder = ["golden ticket"]
    antidote_recipe_folder = ["blueberry antidote recipe piece 1"]
    
    cauldron = []
    cauldron_attempts_left = 2
    antidote_ingredients_list = ["blueberry extract", "deflation gumdrops", "fruity tooty lollipop", "purple taffy", "secret formula"]
    lollipop_recipe_list = ["strawberry","huckleberry","orange syrup"]
    
    available_taffy = ["red taffy","yellow taffy", "blue taffy"]
    
    available_syrup = ["apple syrup", "orange syrup", "banana syrup"]
    
    extract_cabinet = ["raspberry extract", "strawberry extract", "blueberry extract"]
    berries_cabinet = ["huckleberry", "cranberry", "strawberry", "stRaNGe bERrY"]
    
    room_solved = False
    char_is_dead = False
    
    def get_recipes_from_bag():
        recipes_list = []
        for item in bag:
            if "recipe" in item:
                recipes_list.append(item)
        return recipes_list
    
    display("Welcome to the Inventing Room! You are standing in the very place where some of Wonka's world-reknown, best-selling candy concoctions came to life!")
    enter()
    display("You stumbled upon a leftover piece of Three Course Dinner Chewing Gum from Violet Beauregarde's unfortunate mishap.")
    enter()
    display("The curious chap that you are, you gave it a try and suddenly you have turned into a blueberry!")
    enter()
    display("You have grown too large to fit through the doorway in which you entered, and the only way to get out is by creating an antidote and returning to normal size.")
    enter()
    display("Luckily, the Inventing Room is stocked with candy syrups, berries, and other ingredients. Have a look around and perhaps you'll find what you need to whip up an antidote! Good luck!")
    enter()
    
    
    while (not room_solved):
        
        display("What would you like to do?\n\n1 = explore room\n2 = view location descriptions\n3 = view a recipe\n4 = give up")
        r = get_r(["1","2","3","4"])
        
        #explore room
        
        if r == "1":
            explore_room = True
            while(explore_room):
                display("Where would you like to go?\n\n1 = closet\n2 = recipe cabinet\n3 = cauldron\n4 = candy making station\n5 = candy tasting table\n6 = syrup table\n7 = stock pantry\nq = quit")
                r = get_r(["1","2","3","4","5","6","7","q"])
                
                #closet -----------------------------------------------------------
                if r == "1":
                    if "key" not in bag:
                        display("The closet is locked! You cannot open it.")
                        enter()
                    if "key" in bag:
                        display("It looks like the key you found can open the closet. Would you like to open it?\n\ny = yes\nn = no")
                        r = get_r(["y","n"])
                        if r == "y":
                            if len(cabinet_contents) == 0:
                                display("The cabinet is empty.")
                                enter()
                            if "secret formula" in cabinet_contents:
                                display("There is a small vile with a mysterious blue liquid. What would you like to do?\n\n1 = put in bag\n2 = drink the liquid\n3 = leave in closet")
                                r = get_r(["1","2","3"])
                                if r == "1":
                                    bag.append("secret formula")
                                    cabinet_contents.remove("secret formula")
                                    display("You have added <SECRET FORMULA> to your bag.")
                                    enter()
                                if r == "2":
                                    display("The liquid is too strong on its own! Are you sure you would like to drink it?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        display("The liquid was too strong to digest. You have lost a life!")
                                        char_is_dead = True
                                        enter()
                                        return "fail"
                            if "deflation gumdrops" in cabinet_contents:
                                display("You have found <DEFLATION GUMDROPS>! Would you like to put them in your bag?\n\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    bag.append("deflation gumdrops")
                                    cabinet_contents.remove("deflation gumdrops")
                                    display("You have added <DEFLATION GUMDROPS> to your bag.")
                                    enter()
                                    
                #recipe cabinet ---------------------------------------------------
                elif r == "2":
                    explore_cabinet = True
                    while(explore_cabinet):
                        
                        display("This is the recipe cabinet. Add a recipe to your bag to view it. Which folder would you like to look in?\n\n1 = candy\n2 = chocolates\n3 = antidotes\nq = quit")
                        r = get_r(["1","2","3","q"])
                        
                        #candy recipe folder
                        if r == "1":
                            if len(candy_recipe_folder) == 0:
                                display("The candy recipe folder is empty.")
                                enter()
                            if "fruity tooty lollipop recipe" in candy_recipe_folder:
                                display("Would you like to add the <FRUIT TOOTY LOLLIPOP RECIPE> to your bag?\n\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    bag.append("fruity tooty lollipop recipe")
                                    candy_recipe_folder.remove("fruity tooty lollipop recipe")
                                    display("You have added <FRUITY TOOTY LOLLIPOP RECIPE> to your bag.")
                                    enter()
                            if "groovy grape taffy recipe" in candy_recipe_folder:
                                display("Would you like to add the <GROOVY GRAPE TAFFY RECIPE> to your bag?\n\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    bag.append("groovy grape taffy recipe")
                                    candy_recipe_folder.remove("groovy grape taffy recipe")
                                    display("You have added <GROOVY GRAPE TAFFY RECIPE> to your bag.")
                                    enter()
                            if "twisty tangy twizzlers recipe" in candy_recipe_folder:
                                display("Would you like to add the <TWISTY TANGY TWIZZLERS RECIPE> to your bag?\n\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    bag.append("twisty tangy twizzlers recipe")
                                    candy_recipe_folder.remove("twisty tangy twizzlers recipe")
                                    display("You have added <TWISTY TANGY TWIZZLERS RECIPE> to your bag.")
                                    enter()
                            
                        
                        #chocolate recipe folder
                        elif r == "2":
                            if len(chocolate_recipe_folder) == 0:
                                display("The chocolate recipe folder is empty.")
                                enter()
                            if "golden ticket" in chocolate_recipe_folder:
                                bag.append("Golden Ticket 3")
                                display("You have found a <GOLDEN TICKET>! You have added the <GOLDEN TICKET>to your bag.")
                                enter()
                            
                        
                        #antidote recipe folder
                        elif r == "3":
                            if len(antidote_recipe_folder) == 0:
                                display("The antidote recipe folder is empty.")
                                enter()
                            if "blueberry antidote recipe piece 1" in antidote_recipe_folder:
                                display("Would you like to add the <BLUEBERRY ANTIDOTE RECIPE> to your bag?\n\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    bag.append("blueberry antidote recipe piece 1")
                                    antidote_recipe_folder.remove("blueberry antidote recipe piece 1")
                                    display("You have added <BLUEBERRY ANTIDOTE RECIPE> to your bag. It appears that a piece of the paper has been ripped off...")
                                    enter()
    
                        #exit cabinet
                        elif r == "q":
                            explore_cabinet = False
                
                #cauldron ---------------------------------------------------------
                elif r == "3":
                    explore_cauldron = True
                    while(explore_cauldron):
                        display("What would you like to do?\n\n1 = add ingredient\n2 = view ingredients in cauldron\n3 = empty cauldron\n4 = start cooking\nq = quit")
                        r = get_r(["1","2","3","4","q"])
                        
                        if r == "1":
                            if len(bag) > 0:
                                display("Enter ingredient you would like to add. The ingredient must be in your bag or you will not be able to add it.")
                                r = get_r(bag)
                                bag.remove(r)
                                cauldron.append(r)
                                display("You have added <" + r.upper() + "> to the cauldron.")
                                enter()
                            else:
                                display("Your bag is empty. You cannot add any ingredients.")
                                enter()
                        if r == "2":
                            if len(cauldron) > 0:
                                display_string = ""
                                for i in range(0,len(cauldron)):
                                    display_string += cauldron[i].upper()
                                    if i != (len(cauldron) - 1):
                                        display_string += ", "
                                display("The following ingredient(s) are in the cauldron: " + display_string)
                                enter()
                            else:
                                display("The cauldron is empty.")
                                enter()
                        if r == "3":
                            if len(cauldron) > 0:
                                for ingredient in cauldron:
                                    cauldron.remove(ingredient)
                                    bag.append(ingredient)
                                display("The ingredients in the cauldron have been added back to your bag.")
                                enter()
                            else:
                                display("The cauldron is empty.")
                                enter()
                        if r == "4":
                            can_cook = True
                            
                            #check length
                            if len(cauldron) != 5:
                                can_cook = False
                            
                            #check ingredients
                            for ingredient in cauldron:
                                if ingredient not in antidote_ingredients_list:
                                    can_cook = False
                            
                            display("Are you sure you would like to cook the ingredients in the cauldron?\ny = yes\nn = no")
                            r = get_r(["y","n"])
                            if r == "y":
                                if can_cook:
                                    display("You have created the blueberry antidote! Congratulations!")
                                    enter()
                                    explore_cauldron = False
                                    explore_room = False
                                    room_solved = True
                                    return "success"
                                else:
                                    cauldron_attempts_left -= 1
                                    if cauldron_attempts_left > 0:
                                        display("Oops! The cauldron exploded! One more explosion and you may lose a life!")
                                        enter()
                                        for ingredient in cauldron:
                                            cauldron.remove(ingredient)
                                            bag.append(ingredient)
                                        display("Don't worry though... if you added ingredients, they were returned to your bag.")
                                        enter()
                                    else:
                                        display("The cauldron exploded for the second time! You have lost a life!")
                                        char_is_dead = True
                                        enter()
                                        explore_cauldron = False
                                        explore_room = False
                                        return "fail"
                        if r == "q":
                            explore_cauldron = False
                
                #candy making station ---------------------------------------------
                elif r == "4":
                    explore_station = True
                    while(explore_station):
                        display("What candy would you like to make?\n\n1 = deflation gumdrops\n2 = fruity tooty lollipop\n3 = colored taffy\nq = quit")
                        r = get_r(["1","2","3","q"])
                        
                        if r == "1":
                            display("This machine can no longer make deflation gumdrops! Maybe there are some lying around...")
                            enter()
                        elif r == "2":
                            can_cook = True
                            
                            for ingredient in lollipop_recipe_list:
                                if ingredient not in bag:
                                    can_cook = False
                            
                            if can_cook:
                                print bag
                                bag.remove("strawberry")
                                bag.remove("huckleberry")
                                bag.remove("orange syrup")
                                bag.append("fruity tooty lollipop")
                                print bag
                                display("You created a <FRUITY TOOTY LOLLIPOP>! It has been added to your bag.")
                                enter()
                                display("What is this?? Something shiny appears in the corner of your eye.")
                                enter()
                                display("You look underneath the candy making machine...")
                                enter()
                                bag.append("key")
                                display("You found a <KEY>! It has been added to your bag.")
                                enter()
                            else:
                                display("You do not have the ingredients to make this candy.")
                                enter()
                        elif r == "3":
                            display("What color taffy would you like to make?\n\n1 = orange taffy\n2 = green taffy\n3 = purple taffy")
                            r = get_r(["1","2","3"])
                            
                            if r == "1":
                                display("This machine can no longer make orange taffy!")
                                enter()
                            elif r == "2":
                                display("This machine can no longer make green taffy!")
                                enter()
                            elif r == "3":
                                if "red taffy" in bag and "blue taffy" in bag:
                                    print bag
                                    bag.remove("red taffy")
                                    bag.remove("blue taffy")
                                    bag.append("purple taffy")
                                    print bag
                                    display("You created <PURPLE TAFFY>! it has been added to your bag.")
                                    enter()
                                else:
                                    display("You do not have the right ingredients.")
                                    enter()
                        elif r == "q":
                            explore_station = False
                
                #candy testing table ----------------------------------------------
                elif r == "5":
                    explore_candy_tasting_table = True
                    while(explore_candy_tasting_table):
                        display("What candy would you like to look at?\n\n1 = jolly ranchers\n2 = taffy\n3 = gumdrops\nq = quit")
                        r = get_r(["1","2","3","q"])
                        
                        #jolly ranchers
                        if r == "1":
                            display("Looks like someone ate all the jolly ranchers already. Oops.")
                            enter()
                        elif r == "2":
                            if len(available_taffy) == 0:
                                display("There is no taffy left.")
                                enter()
                            else:
                                available_taffy_string = ""
                                for taffy in available_taffy:
                                    available_taffy_string += taffy + "\n"
                                    
                                display("The following taffy is on the table. Which would you like to look at?\n\n" + available_taffy_string)
                                r = get_r(available_taffy)
                                
                                if r == "red taffy":
                                    display("Would you like to add the <RED TAFFY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("red taffy")
                                        available_taffy.remove("red taffy")
                                        display("You have added <RED TAFFY> to your bag.")
                                        enter()
                                elif r == "yellow taffy":
                                    display("Would you like to add the <YELLOW TAFFY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("yellow taffy")
                                        available_taffy.remove("yellow taffy")
                                        display("You have added <YELLOW TAFFY> to your bag.")
                                        enter()
                                elif r == "blue taffy":
                                    display("Would you like to add the <BLUE TAFFY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("blue taffy")
                                        available_taffy.remove("blue taffy")
                                        display("You have added <BLUE TAFFY> to your bag.")
                                        enter()
                                        
                        elif r == "3":
                            display("These gumdrops have been sitting here for a few months. You probably don't wanna touch 'em.")
                            enter()
                        elif r == "q":
                            explore_candy_tasting_table = False
                
                #syrup table ------------------------------------------------------
                elif r == "6":
                    available_syrup_string = ""
                    for syrup in available_syrup:
                        available_syrup_string += syrup + "\n"
                        
                    display("The following syrup is on the table. Which would you like to look at?\n\n" + available_syrup_string)
                    r = get_r(available_syrup)
                    
                    if r == "apple syrup":
                        display("This syrup is way too sticky to touch.")
                        enter()
                    elif r == "orange syrup":
                        display("Would you like to add the <ORANGE SYRUP> to your bag?\n\ny = yes\nn = no")
                        r = get_r(["y","n"])
                        if r == "y":
                            bag.append("orange syrup")
                            available_syrup.remove("orange syrup")
                            display("You have added <ORANGE SYRUP> to your bag.")
                            enter()
                            display("Hmm... it looks like there is a piece of paper underneath the extract bottle. It looks like part of a recipe.")
                            enter()
                            bag.append("blueberry antidote recipe piece 3")
                            display("You have added <BLUEBERRY ANTIDOTE RECIPE PIECE 3> to your bag.")
                            enter()
                    elif r == "banana syrup":
                        display("Looks like the Oompa Loompas need to restock the banana syrup.")
                        enter()
                        
                
                #stock pantry -----------------------------------------------------
                elif r == "7":
                    explore_pantry = True
                    while(explore_pantry):
                        display("Which cabinet would you like to look in?\n\n1 = extracts\n2 = berries\nq = quit")
                        r = get_r(["1","2","q"])
                        
                        #extract cabinet
                        if r == "1":
                            if len(extract_cabinet) == 0:
                                display("The extract cabinet is empty.")
                                enter()
                            else:
                                extracts_in_cabinet = ""
                                for extract in extract_cabinet:
                                    extracts_in_cabinet += extract + "\n"
                                    
                                display("The following extracts are in the cabinet. Which would you like to look at?\n\n" + extracts_in_cabinet)
                                r = get_r(extract_cabinet)
    
                                if r == "raspberry extract":
                                    display("Would you like to add the <RASPBERRY EXTRACT> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("raspberry extract")
                                        extract_cabinet.remove("raspberry extract")
                                        display("You have added <RASPBERRY EXTRACT> to your bag.")
                                        enter()
                                elif r == "strawberry extract":
                                    display("Would you like to add the <STRAWBERRY EXTRACT> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("strawberry extract")
                                        extract_cabinet.remove("strawberry extract")
                                        display("You have added <STRAWBERRY EXTRACT> to your bag.")
                                        enter()
                                elif r == "blueberry extract":
                                    display("Would you like to add the <BLUEBERRY EXTRACT> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("blueberry extract")
                                        extract_cabinet.remove("blueberry extract")
                                        display("You have added <BLUEBERRY EXTRACT> to your bag.")
                                        enter()
                                        display("Hmm... it looks like there is a piece of paper underneath the extract bottle. You pick it up and appears to be part of a recipe.")
                                        enter()
                                        bag.append("blueberry antidote recipe piece 2")
                                        display("You have added <BLUEBERRY ANTIDOTE RECIPE PIECE 2> to your bag.")
                                        enter()
                            
                        #berries cabinet
                        elif r == "2":
                            if len(berries_cabinet) == 0:
                                display("The berries cabinet is empty.")
                                enter()
                            else:
                                berries_in_cabinet = ""
                                for berry in berries_cabinet:
                                    berries_in_cabinet += berry + "\n"
                                
                                display("The following berries are in the cabinet. Which would you like to look at?\n\n" + berries_in_cabinet)
                                r = get_r(berries_cabinet)
                                
                                if r == "huckleberry":
                                    display("Would you like to add the <HUCKLEBERRY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("huckleberry")
                                        berries_cabinet.remove("huckleberry")
                                        display("You have added <HUCKLEBERRY> to your bag.")
                                        enter()
                                elif r == "cranberry":
                                    display("Would you like to add the <CRANBERRY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("cranberry")
                                        berries_cabinet.remove("cranberry")
                                        display("You have added <CRANBERRY> to your bag.")
                                        enter()
                                elif r == "strawberry":
                                    display("Would you like to add the <STRABERRY> to your bag?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "y":
                                        bag.append("strawberry")
                                        berries_cabinet.remove("strawberry")
                                        display("You have added <STRAWBERRY> to your bag.")
                                        enter()
                                elif r == "stRaNGe bERrY":
                                    display("What would you like to do with the <stRaNGe bERrY>?\n\n1 = eat the berry\n2 = add it to your bag\n3 = nothing")
                                    r = get_r(["1","2","3"])
                                    if r == "1":
                                        display("Uh oh! The berry is poisonous! You have lost a life!")
                                        char_is_dead = True
                                        enter()
                                        return "fail"
                                    elif r == "2":
                                        bag.append("stRaNGe bERrY")
                                        berries_cabinet.remove("stRaNGe bERrY")
                                        display("You have added <stRaNGe bERrY> to your bag.")
                                        enter()
                                        explore_pantry = False
                                        explore_room = False
                        elif r == "q":
                            explore_pantry = False
                            
                elif r == "q":
                    explore_room = False
                
        #view location descriptions
        elif r == "2":
            view_loc_desc = True
            while(view_loc_desc):
                display("What would you like to know more about?\n1 = closet\n2 = recipe cabinet\n3 = cauldron\n4 = candy making station\n5 = candy tasting table\n6 = syrup table\n7 = stock pantry\nq = quit")
                r = get_r(["1","2","3","4","5","6","7","q"])
                
                if r == "1":
                    display("Cabinet\nHolds some secret stuff. Wonka usually keeps it locked for some reason...")
                    enter()
                elif r == "2":
                    display("Recipe Cabinet\nHolds recipes for various candies, chocolates, and antidotes (in case of emergency).")
                    enter()
                elif r == "3":
                    display("Cauldron\nWhere you can cook up an antidote. Make sure you have all the ingredients you need!")
                elif r == "4":
                    display("Candy Making Station\nWhere you can melt down candies, combine candies and ingredients to make new candies, or make a concoction of your own! The possibilities are endless.")
                elif r == "5":
                    display("Candy Tasting Table\nWhere you can find candies currently in production and have a taste!")
                elif r == "6":
                    display("Syrup Table\nWhere you can find various colored and flavored syrups stored in glass containers.")
                elif r == "7":
                    display("Stock Pantry\nWhere you can find ingredients like berries and extracts.")
                elif r == "q":
                    view_loc_desc = False
        
        #view recipes
        elif r == "3":
            recipes_list = get_recipes_from_bag()
            if len(recipes_list) == 0:
                display("You have no recipes in your bag. Add a recipe to view it.")
                enter()
            else:
                view_recipes = True
                recipes_list.append("q")
                while(view_recipes):
                    display("Enter recipe you would like to view. The recipe must be in your bag or you will not be able to view it. Enter 'q' to quit")
                    r = get_r(recipes_list)
                    if r == "q":
                        view_recipes = False
                    elif r == "fruity tooty lollipop recipe":
                        display("To create a <FRUITY TOOTY LOLLIPOP>, you need 3 things:\n1) 1 strawberry\n2) 1 huckleberry\n3) 1 flask of orange syrup")
                        enter()
                    elif r == "groovy grape taffy recipe":
                        display("This appears to be an old recipe... The words are too faded to make out.")
                        enter()
                    elif r == "twisty tangy twizzlers recipe":
                        display("This appears to be an old recipe... The words are too faded to make out.")
                        enter()
                    elif r == "blueberry antidote recipe piece 1":
                        display("To create a <BLUEBERRY ANTIDOTE>, you need 5 things:\n1) blueberry extract\n2) secret formula\n3) deflation gumdrops\n\nthe rest of the recipe appears to be ripped off...")
                        enter()
                    elif r == "blueberry antidote recipe piece 2":
                        display("4) purple taffy\n\nhint: maybe mix taffy colors in the candy making station...?\n\nthe rest of the recipe appear to be ripped off...")
                        enter()
                    elif r == "blueberry antidote recipe piece 3":
                        display("5) fruity tooty lollipop\n\nCombine these ingredients in a cauldron, and your antidote is complete!")
                        enter()
        
        elif r == "4":
            display("Your progress will not be saved and items you have picked up in this room will not remain in your bag. Would you like to continue?\ny = yes\nn = no")
            r = get_r(["y","n"])
            if r == "y":
                display("You have left the room.")
                enter()
                return

#Squirrel room function
def runSquirrelRoom():
    global bag
    displayTitle('Squirrel Room')
    displayRoomImage('squirrelroom.png')
    display('Welcome to the Squirrel Room! You are standing in the middle of a garbage chute where dozens of squirrels are rumaging around.')
    enter()
    display('One squirrel comes up to you and asks, "Can you help us lift our nuts onto the other pole?"')
    enter()
    display('Well that\'s pretty easy isn\'t it? you think to yourself. Would you like to help?\n\ny = yes\nn = no')
    r = get_r('yn')
    if r == 'y':
        display('Squirrel: "Yay! Let\'s get down to business. None of us squirrels could figure it out."')
        enter()
        display('Squirrel: "We\'re also kind of hungry though, so if you can\'t complete it in time, we\'ll probably have to eat you instead."')
        enter()
        display('Squirrel: "If you want to take the easy way out, let\'s just play a game of rock paper scissors. If you win, we\'ll give you a prize. If I win, we get to eat you."\n\n1 = rock paper scissors\n2 = help them move their nuts')
        r = get_r('12')
        if r == '1':
            display('Squirrel: "Sounds good to me. Ready..."')
            enter()
            tie = True
            while(tie):
                display('Squirrel: "Rock... paper... scissors..."\n\nr = rock\np = paper\ns = scissors')
                r = get_r('rps')
                squir = random.choice('rps')
                if r == 'r' and squir == 'p':
                    display('...shoot!\nYes! I had paper! Fellas, it\'s time for lunch.')
                    enter()
                    display('The squirrels eat you.')
                    enter()
                    return 'fail'
                elif r == 'r' and squir == 's':
                    display('...shoot!\nAw man, I had scissors. You got me. Here\'s the golden ticket you wanted.')
                    enter()
                    display('Congratulations! The golden ticket has been added to your backpack.')
                    bag.append('Golden Ticket 4')
                    enter()
                    return 'success'
                elif r == 's' and squir == 'p':
                    display('...shoot!\nAw man, I had paper. You got me. Here\'s the golden ticket you wanted.')
                    enter()
                    display('Congratulations! The golden ticket has been added to your backpack.')
                    bag.append('Golden Ticket 4')
                    enter()
                    return 'success'
                elif r == 's' and squir == 'r':
                    display('...shoot!\nYes! I had rock! Fellas, it\'s time for lunch.')
                    enter()
                    display('The squirrels eat you.')
                    enter()
                    return 'fail'
                elif r == 'p' and squir == 'r':
                    display('...shoot!\nAw man, I had rock. You got me. Here\'s the golden ticket you wanted.')
                    enter()
                    display('Congratulations! The golden ticket has been added to your backpack.')
                    bag.append('Golden Ticket 4')
                    enter()
                    return 'success'
                elif r == 'p' and squir == 's':
                    display('...shoot!\nYes! I had scissors! Fellas, it\'s time for lunch.')
                    enter()
                    display('The squirrels eat you.')
                    enter()
                    return 'fail'
                elif r == squir:
                    display('We tied. Let\'s go again')
                    enter()
        elif r == '2':
            display('"Alright, so here\'s the deal. It\'s pretty much like the Tower of Hanoi if you\'ve heard of that puzzle."\n\ny = yes, I know that puzzle\nn = no, I need a refresher')
            r = get_r('yn')
            if r == 'y':
                display('So it\'s the same deal here. You get three poles and you have to move the nuts onto the last pole in the order 1, 2, 3)')
                enter()
                display('Remember, you can\'t place a larger nut (3>2>1) on a smaller nut.')
            elif r == 'n':
                display('So basically, there are 3 poles. The 3 nuts start on one pole from smallest to biggest (1,2,3).')
                enter()
                display('Using all three poles, you get to move the nuts one at a time to get to get the nuts on the last pole in the order 1,2,3.')
                enter()
                display('You can\'t place a larger nut (3>2>1) on a smaller nut.')
                enter()
            pole1 = ['1','2','3']
            pole2 = [' ',' ',' ']
            pole3 = [' ',' ',' ']
            unsolved = True
            count = 0
            while(unsolved):
                poleString = printPoles(pole1,pole2,pole3)
                display(poleString + 'Which number nut would you like to move?')
                nutnum = get_r(isFirstPole(pole1,pole2,pole3))
                display(poleString + 'Which pole would you like to move it to?')
                polenum = get_r(isPoleOk(nutnum, pole1,pole2,pole3))
                oldpole = findOldPole(nutnum,pole1,pole2,pole3)
                if polenum == '1':
                    editPoles(nutnum,oldpole,pole1)
                elif polenum == '2':
                    editPoles(nutnum,oldpole,pole2)
                elif polenum == '3':
                    editPoles(nutnum,oldpole,pole3)
                unsolved = checkCorrect(pole3)
                count+=1
                if count%5 == 0:
                    display('Would you like to quit? You\'ll lose a life.\n\nq = quit\nn = no, continue')
                    r = get_r('qn')
                    if r == 'q':
                        return 'fail'
            display('Wow! Thanks for helping us move our nuts! As a gift, we\'ll give you a golden ticket!')
            bag.append('Golden Ticket 4')
            enter()
            display('You will return to home.')
            enter()
    elif r == 'n':
        display('You have left the room.')
        return

# Squirrel room helper functions
def checkCorrect(pole):
    if pole == ['1','2','3']:
        return False
    return True

def findOldPole(num,pole1,pole2,pole3):
    if num in pole1:
        return pole1
    elif num in pole2:
        return pole2
    elif num in pole3:
        return pole3

def firstNumIndex(pole):
    for num in pole:
        if num != ' ':
            print num
            return num
    return ' '

def isPoleOk(num,pole1, pole2, pole3):
    editable = ''
    poleArray = [' ',pole1, pole2, pole3]
    for i in range(1,4):
        firstNum = firstNumIndex(poleArray[i])
        if firstNum == ' ':
            editable += str(i)
        elif int(firstNum)>int(num):
            editable += str(i)
    print editable
    return editable

def editPoles(num,oldpole,newpole):
    editIndex = oldpole.index(num)
    oldpole[editIndex] = ' '
    for i in range(2,-1,-1):
        if newpole[i] == ' ':
            newpole[i] = num
            print 'yes'
            return newpole
    newpole[0] = num
    return newpole

def printPoles(pole1,pole2,pole3):
    displayString = ''
    displayString += 'pole1:   '
    for num in pole1:
        displayString += '  ' + num + '  '
    displayString += '\npole2:   '
    for num in pole2:
        displayString += '  ' + num + '  '
    displayString += '\npole3:   '
    for num in pole3:
        displayString += '  ' + num + '  '
    displayString += '\n'
    return displayString

def isFirstPole(pole1,pole2,pole3):
    validInput = []
    for pole in [pole1,pole2,pole3]:
        if pole[0] != ' ':
            validInput.append(pole[0])
        else:
            if pole[1] != ' ':
                validInput.append(pole[1])
            else:
                if pole[2] != ' ':
                    validInput.append(pole[2])
    return validInput


#TV Room function
def runTVRoom():
    displayTitle('TV Room')
    displayRoomImage('tvroom.png')
    room_solved = False
    questions_done = False
    oompa_called = False
    machine_wired = False
    run_machine = False
    bag = []

    display("Now, you are in the TV Room, where Mike Teavee had his unpleasant incident during the miniaturization display.")
    enter()
    display("You take a look around the room and observe many strange objects and machinery.")
    enter()

    while not room_solved:

        display("What would you like to do?\n\n1 = explore room\n2 = leave room")
        r = get_r(["1","2"])

        #explore room
        if r == "1":
            display("What would you like to explore?\n\n1 = large piece of machinery in the middle of the room\n2 = table covered in wires\n3 = vintage TV set\nq = quit")
            r = get_r(["1","2","3","q"])

            #machinery in center
            if r == "1":
                if not machine_wired and not run_machine:
                    if "wires" not in bag:
                        display("As you approach the intimidating machine, you see a button on its side.")
                        enter()
                        display("Curiosity courses through your mind as you get closer to the button.")
                        enter()
                        display("You put your finger on the button and hesitate, remembering the Mike Teavee incident.")
                        enter()
                        display("The curiosity gets the best of you. You close your eyes and press the b.utton")
                        enter()
                        display("...")
                        enter()
                        display("And you wait.")
                        enter()
                        display("Nothing happens.")
                        enter()
                        display("Suddenly, you notice that the wires attached to the back of the machine are frayed and broken. No wonder the machine didn't work!")
                        enter()
                        display("Somewhat relieved, you decide to explore a different part of the room and leave the machine.")
                        enter()
                    elif "wires" in bag:
                        display("As you get approach the machine, you see broken wires attaching it to the ceiling.")
                        enter()
                        display("You get closer and also see a red button on the side of the machine.")
                        enter()
                        while not machine_wired:
                            display("What would you like to do?\n\n1 = get the Oompa Loompa to help you rewire machine\n2 = try to rewire machine yourself\n3 = leave and explore something else")
                            r = get_r(["1","2","3"])
                            if r == "1":
                                if not oompa_called:
                                    display("You realize that the Oompa Loompa never told you his name.")
                                    enter()
                                    display("\"Uhh...\" you begin.")
                                    enter()
                                    display("\"Mister... Oompa Loompa man?\" you hesitantly call out. \"I need some help...\"")
                                    enter()
                                    display("There is no response.")
                                    enter()
                                    display("You try again. \"Sir Oompa Loompa? Dr. Loompa? Are you there??\"")
                                    enter()
                                    display("Still no reply.")
                                    enter()
                                    display("You are running out of names to call out. \"Little... orange man?\"")
                                    enter()
                                    display("\"WHAT DID YOU JUST CALL ME?\" a voice booms out.")
                                    enter()
                                    display("You blink and the Oompa Loompa appears. \"Hey there,\" you say. \"Thanks for coming.\"")
                                    enter()
                                    display("He looks at me for a second and then rolls his eyes. \"Yeah, whatever. What do you want? It better not be something stupid because I stopped eating my chocolate pudding for this...\"")
                                    enter()
                                    display("You hold out the wires from before. \"Do you think you can help me rewire the machine?\"")
                                    enter()
                                    display("He looks you in the eyes. \"Are you sure? That machine can be pretty dangerous...\"")
                                    enter()
                                    display("Are you sure you want to continue?\n\ny = yes\nn = no")
                                    r = get_r(["y","n"])
                                    if r == "n":
                                        oompa_called = True
                                        display("\"Maybe not,\" you say. \"It's probably too dangerous.\"")
                                        enter()
                                        display("The Oompa Loompa shrugs. \"Whatever,\" he says. \"Your choice. I'm going to go back to my pudding now.\"")
                                        enter()
                                        break
                                    display("\"Yeah, I'm sure,\" you say. \"Let's do it.\"")
                                    enter()
                                    display("\"Alright,\" the Oompa Loompa shrugs. \"Your call. Hand over the wires and I'll take care of it. Just don't call me little orange man again.\"")
                                    enter()
                                    display("You hand over the wires and the Oompa Loompa gets to work. Soon enough, he finishes. \"All done,\" he calls out. \"Now I'm going to go back to that pudding. My lunch break is almost over, so don't bother me again.\"")
                                    enter()
                                    display("Machine successfully wired!")
                                    machine_wired = True
                                    display("Would you like to run the machine?\ny = yes\nn = no")
                                    r = get_r("y","n")
                                    if r == "y":
                                        run_machine = True
                                elif oompa_called:
                                    display("\"Hey, little orange man!\" you call out.")
                                    enter()
                                    display("The Oompa Loompa appears. \"You really have to quit calling me that, kid,\" he grumbles.")
                                    enter()
                                    display("\"I changed my mind,\" you declare. \"Can you help me wire the machine?\"")
                                    enter()
                                    display("The Oompa Loompa rolls his eyes. \"You better not be messing with me. I was in the middle of eating my chocolate sundae.\"")
                                    enter()
                                    display("\"I'm sure this time,\" you say. \"Here are the wires.\"")
                                    enter()
                                    display("\"Alright,\" he sighs. \"I'll do it. But don't be calling me again, ok? I want to eat my food.\"")
                                    enter()
                                    display("Finally, he gets to work, grumbling about how this was the worst lunch break he's ever had. You feel bad bothering him, but you really want to know more about the machine.")
                                    enter()
                                    while not questions_done:
                                        display("What would you like to ask him?\n1 = \"What does the machine do?\"\n2 = \"How did the machine break?\"\nq = quit")
                                        r = get_r(["1","2","q"])
                                        if r == "1":
                                            display("\"This is what Mr. Wonka likes to call the 'Minimizing Machine.'\"")
                                            enter()
                                            display("\"When you press the red button, it will shrink whatever you put in front of it and transports it to the TV over there.\"")
                                            enter()
                                            display("\"He wants to use it to send chocolate to the public through their TV sets. He calls it 'Television Chocolate'.\"")
                                            enter()
                                            display("\"Is there a way to reverse the shrink way and make things bigger?\" you ask.")
                                            enter()
                                            display("\"Yes, actually,\" he replies. \"After the incident with Mike Teavee, we decided to put a button in the TV that can reverse the works of the shrink ray.\"")
                                            enter()
                                        elif r == "2":
                                            display("\"One of the old Oompa Loompa workers, Jerry, tried to shrink the TV once. It ended up cracking the TV in half, and fried all of the wires on the machine.\"")
                                            enter()
                                            display("\"Needless to say, he was fired.\"")
                                            enter()
                                            display("\"We replaced the TV with one of our backups, but we didn't get the chance to replace the wires yet. So I guess it's good that you're making me do this now, even though it is supposed to be my break...\"")
                                            enter()
                                        elif r == "q":
                                            questions_done = True
                                    display("Eventually, he finishes, nods at me and disappears, presumably back to his sundae.")
                                    enter()
                                    display("Machine successfully wired!")
                                    machine_wired = True
                                    display("Would you like to run the machine?\ny = yes\nn = no")
                                    r = get_r("y","n")
                                    if r == "y":
                                        run_machine = True
                            elif r == "2":
                                display("You don't want to bother the Oompa Loompa and his lunch again, so you decide to wire the machine yourself. It can't be THAT difficult.")
                                enter()
                                display("You get to work, and everything goes smoothly. The wires are the right size and it is pretty easy to figure out what goes where.")
                                enter()
                                display("Finally, you get to the last wire connection. You reach up to plug the wire into the socket in the ceiling with a feeling of satisfaction.")
                                enter()
                                display("Suddenly, you feel your foot slip from under you. You instinctually grab the wires to catch yourself. Unfortunately, you grab open part of the wire connected to the celing and die from electric shock.")
                                enter()
                                display("You have failed! Better luck next time!")
                                enter()
                                return "failed"
                            elif r == "3":
                                display("You leave the machine.")
                                break
                elif machine_wired and run_machine:
                    display("What would you like to shrink?\n1 = the chocolate bar\n2 = the TV\n3 = yourself\nq = quit")
                    r = get_r("1","2","3")
                    if r == "1":
                        display("You position the chocolate bar to make sure it is under the shrink ray.")
                        enter()
                        display("You press the button and ZAP!")
                        enter()
                        display("There is a huge flash of white light, and the giant piece of chocolate disappears!")
                        enter()
                        display("You look over at the TV and see a smaller version of the chocolate bar in the screen.")
                        enter()
                        display("Hesitant, but hungry, you reach into the TV screen and pull out the chocolate bar.")
                        enter()
                        display("When you open it, there is a motivational quote on the inside of the wrapper.")
                        enter()
                        display("\"Don't be afraid to take a risk!\" it encourages you.")
                        enter()
                        display("'What a cute message!' you think to yourself as you take a bite of the chocolate.")
                    elif r == "2":
                        display("Remembering the Oompa Loompa's story about Jerry, you decide to take a risk and try to recreate the incident. You are desperate and need to get out of this factory soon.")
                        enter()
                        display("You drag the TV over from the corner and set it on the pedestal in front of the machine. You go over to the button and press it.")
                        enter()
                        display("ZAP! There is a huge flash of white light and a big cracking noise. The ground begins shaking, and you fear that the ceiling will cave in on you.")
                        enter()
                        display("Eventually, everything calms down. The smell of fried metal fills the air. You look down at the TV, and sure enough, it is split in half. A thin trail of smoke sneaks up from it.")
                        enter()
                        display("You look around the rubble, trying to find something, but to no avail. Disappointed, you turn away. Where is that last golden ticket?")
                        enter()
                        display("Suddenly, a glint of something shiny catches your eye from behind the broken TV screen. Could it be...?")
                        enter()
                        display("You investigate closer, and sure enough, it is the golden ticket! The answer was \"within\" the TV all along...")
                        enter()
                        display("Congratulations. You found the golden ticket!")
                        bag.append("Golden Ticket 5")
                        enter()
                        return "success"
                    elif r == "3":
                        display("Out of curiosity, you decide to try to shrink yourself.")
                        enter()
                        display("Ever since the Mike Teavee incident, you had always wondered what it felt like to be shrunken. And anyways, the Oompa Loompa said that it was reversible.")
                        enter()
                        display("You step up on the platform and reach over and press the red button on the side of the machine.")
                        enter()
                        display("ZAP! You are surrounded by a white light and the most surreal feeling rushes over you. Your body feels like mist, and you can feel the particles in your body moving around. However, it is not painful.")
                        enter()
                        display("Eventually, you open your eyes and you find yourself looking out of the screen of what you assume is the TV. You are tiny!")
                        enter()
                        display("You look around at your surroundings and are amazed at their simplicity.")
                        enter()
                        display("Suddenly, you see something sparkle out of the corner of your eye,")
                        enter()
                        display("Fascinated, you turn your head and move a little closer. Is that what you think it is...")
                        enter()
                        display("You investigate closer, and sure enough, it is the golden ticket! The answer was \"within\" the TV all along...")
                        enter()
                        display("Congratulations. You found the golden ticket!")
                        bag.append("Golden Ticket 5")
                        enter()
                        return "success"
                    elif r == "q":
                        display("You leave the machine.")
                        enter()
            #explore table
            elif r == "2":
                if "wires" not in bag and not machine_wired:
                    display("As you get closer to the table, you take a closer look at the wires.")
                    enter()
                    display("There are two wires on the table, one red and one blue.")
                    enter()
                    display("You feel like the wires may be useful to you later on.")
                    enter()
                    display("Do you want to take the <Wires>?\n\ny = yes\nn = no\nq = quit")
                    r = get_r(["y","n","q"])
                    if r == "y":
                        bag.append("wires")
                        display("<Wires> are added to your bag.")
                        enter()
                        display("\"Hey!\" someone suddenly yells. \"What are you doing here?!\"")
                        enter()
                        display("You whirl around from your bag and come face to face with an anry-looking Oompa Loompa")
                        enter()
                        display("How do you want to respond? You don't think he saw you take the wires, but you are not sure.\n1 = yell back at him\n2 = apologize for taking wires\n3 = lie to him")
                        r = get_r(["1","2","3"])
                        if r == "1":
                            display("\"What do you think I'm doing?!\" you yell back defiantly. This was the last straw. Being stuck in this factory is messing with your mind.")
                            enter()
                            display("\"It's not my fault that I'm stuck in this stinking factory!")
                            enter()
                            display("\"I'm just trying to find some way to get out of here, and I don't need meddling little orange men poking around in my business!")
                            enter()
                            display("The Oompa Loompa is silent for a second.")
                            enter()
                            display("Eventually, he sighs. \"Look, buddy,\" he sighs. \"I don't want to yell at you as much as you don't want me to. I'm on my lunch break and the last thing I want to be doing is be the security man of the TV Room.")
                            enter()
                            display("\"And I get why you're so frustrated,\" he continues. \"I've been stuck here my whole life. But you don't have to be so rude. Did you really have to call me a little orange man? That's low, man. Didn't your parents teach you some manners?\"")
                            enter()
                            display("\"Sorry about that,\" you look down, sheepish. \"I just got a little overwhelmed\"")
                            enter()
                            display("\"It's alright. I feel for you, kid,\" he says. \"Well, my candy sandwich is calling my name from the other room. Don't cause any trouble here; I won't be as easy on your next time!\"")
                            enter()
                            display("\"I promise I won't,\" I assure him. \"Enjoy your lunch!\"")
                            enter()
                            display("\"I will,\" he calls, already walking out. \"If you need something, holler for me. But only in emergencies! I want to enjoy my lunch in peace...\"")
                            enter()
                            display("And then he was gone. Your sigh of relief echoes in the silent room. You double check your bag to make sure the <Wires> are still there. They are. That was a close call.")
                            enter()
                        elif r == "2":
                            display("\"Sir, I am so so so sorry,\" you stammer. \"I'm just trying to find some way to get out of this factory so I can go back to my family, and I really don't want to cause any trouble.\"")
                            enter()
                            display("\"I really didn't know that I wasn't supposed to take the wires, and I am so so so sorry. If you need to arrest me, I understand,\" you say with a bowed head.")
                            enter()
                            display("The Oompa Loompa just stares at you. Then, out of nowhere, he starts laughing.")
                            enter()
                            display("It starts out with little giggles and ends with him bent over, howling and gasping for air.")
                            enter()
                            display("You just stare at him, confused. Eventually, he calms down.")
                            enter()
                            display("\"You humans are so strange,\" he chuckles, turning back to you and wiping tears from his eyes.")
                            enter()
                            display("You keep on staring at him. What just happened?!")
                            enter()
                            display("\"Alright look, kid,\" he sighs. \"I didn't even see you take the wires, but I'm technically supposed to report you to the boss for stealing.")
                            enter()
                            display("You look at him with fear in my eyes. You'll never be able to find the last golden ticket if you're arrested.")
                            enter()
                            display("\"But,\" he continues, \"since you made me laugh, I'll let you slide this time.\"")
                            enter()
                            display("You let out a sigh of relief. \"Thanks,\" you say.")
                            enter()
                            display("\"Yeah, whatever,\" he says. \"But if this happens again, I won't be able to help you again, though. So be careful!\"")
                            enter()
                            display("\"I promise I won't,\" you assure him.")
                            enter()
                            display("\"Well,\" he says, looking at his watch, \"it's my lunch break and my candy sandwich is calling my name from the other room, so I better get going. Good luck, old sport.\"")
                            enter()
                            display("And then he disappears, leaving you standing in the middle of this strange room, unsure of what just happened.")
                        elif r == "3":
                            display("\"Hello, sir,\" you say smoothly, subtly zipping up your incriminating backpack. \"I'm Charlie Bucket (the one from the famous movies and books), and I was just passing through. Just like old times, you know?\"")
                            enter()
                            display("The Oompa Loompa looks at you skeptically. \"Just 'passing through'?\" he asks.")
                            enter()
                            display("You nod enthusiastically. \"It's been a great trip down memory lane. I'll be on my way soon, though. It's getting late. \"")
                            enter()
                            display("\"Alright...\" His beady eyes drill into me.")
                            enter()
                            display("Just then, he looks over at the table with the missing wires. You see the flash of realization in his eyes as he looks over at your bag. \"What happened to the wires over there?!\"")
                            enter()
                            display("You hold your breath as he makes eye contact with you.")
                            enter()
                            display("He narrows his eyes. \"Give me your bag,\" he demands, holding out his hand. You hesitate at first, but reluctantly hand over the bag when you realize you don't have any choice.")
                            enter()
                            display("You look down at your feet as he pulls out the stolen wires from your bag. \"Come with me,\" he growls, grabbing your arm.")
                            enter()
                            display("\"Where are we going?\" you ask tentatively.")
                            enter()
                            display("\"Where we send all of the factory intruders and liars,\" he replies. \"All you need to know is that you won't see the outside world again for a very long time, if ever.\"")
                            enter()
                            display("\"Next time, think twice before lying. It'll always come back to bite you...\"")
                            enter()
                            display("You have failed! Better luck next time!")
                            enter()
                            return "failed"
                    elif r == "n":
                        display("Wires are left as they are.")
                        enter()
                        display("You leave the table.")
                        enter()
                    else:
                        display("You leave the table.")
                        enter()
                elif "wires" in bag or machine_wired:
                    display("There is nothing left at the table.")
                    enter()
                    display("You leave the table.")
                    enter()
            #explore tv set
            elif r == "3":
                display("You approach the old TV set in the corner of the room.")
                enter()
                display("Do you want to turn it on?\n\ny = yes\nn = no\q = quit")
                r = get_r(["y","n","q"])
                if r == "y":
                    display("You find the power button on the old machine, and the TV sputters on.")
                    enter()
                    display("There is a strange message on the TV screen.\n\"The answer is always within.\"")
                    enter()
                    display("What could this mean?")
                    enter()
                elif r == "n":
                    display("TV is left off.")
                    enter()
                    display("You leave the TV.")
                    enter()
                elif r == "q":
                    display("You leave the TV.")
                    enter()
        #leave room
        elif r == "2":
            display("Your progress will not be saved and items you have picked up in this room will not remain in your bag. Would you like to continue?\ny = yes\nn = no")
            r = get_r(["y","n"])
            if r == "y":
                display("You have left the room.")
                enter()
                break

def runFinalRoom():
    displayTitle('Final Room')
    displayRoomImage('finalroom.png')
    display("As you walk through the gleaming gold doors, a shiver runs through your body.")
    enter()
    display("You have reached the final step. You have no idea what to expect.")
    enter()
    display("You look around the room and see shelves and shelves of endless books. The shelves seem to go forever, and you can't see the end of the hallway even when you strain your eyes.")
    enter()
    display("Suddenly you hear a low growl behind you...")
    enter()
    display("You turn around and see the largest beast you have ever seen in your life.")
    enter()
    display("Its ruby red eyes gleam at you as it licks its rock candy encrusted lips. The rock candy pieces run down its whole body, scintillating and razor sharp. Two massive wings spread out behind it, muscular and thick with woven twizzlers.")
    enter()
    display("The candy dragon hungrily stares at you as it slowly prowls towards you. What do you do?\n1 = run away\n2 = stay still\n3 = yell for help")
    r = get_r(["1","2","3"])
    if r == "1":
        display("You run as fast as you can towards the door, but the dragon is faster.")
        enter()
        display("He overtakes you and kills you.")
        enter()
        return "failed"
    elif r == "2":
        display("You read somewhere that you should not make any sudden movements when there is a bear that seems like it will attack. This is not necessarily a bear, but it's the closest shot you have.")
        enter()
        display("The dragon gets closer and closer, and you start to back up really slowly.")
        enter()
        display("Soon, you can feel its hot breath on your face, and you close your eyes and say a quick prayer.")
        enter()
        display("Suddenly, you hear a sharp voice. \"Billy!\" it scolds. \"What are you doing?!\"")
        enter()
        display("You hear a pitiful whimper in front of you and the hot breath disappears.")
        enter()
        display("You slowly open your eyes and see the candy dragon cowering under the glare of none other than Willy Wonka himself.")
        enter()
        display("Wonka looks over at you with apologetic eyes. \"Sorry about him,\" he says. \"It's so hard to control all of my little pets all the time.\"")
        enter()
    elif r == "3":
        display("\"Help!\" you scream. \"Someone help me!\"")
        enter()
        display("However, your yelling seems to anger the dragon even more and he pounces, killing you.")
        enter()
        return "failed"
    display("\"Billy!\" Wonka goes back to reprimanding his \"little pet.\" \"We've been over this before: it's rude to eat guests. I've taught you better!\"")
    enter()
    display("The dragon lowers its gleaming head and Wonka gives it a reassuring pat. \"It's alright, buddy, I know it's tough.\"")
    enter()
    display("You stare in disbelief at the spectacle in front of you. What is going on?!")
    enter()
    display("Wonka meets your shocked eyes and laughs out loud. \"Sorry again, pal. I've had Billy for a few years now and he's still learning. He's just a baby. He's really sweet though, and I'm not just talking about his candy scales.\"")
    enter()
    display("You keep on staring at him. You try to open your mouth and reply, but all that comes out is incomprehensible babble. \"Wh-Wha-, Who-, How-\"")
    enter()
    display("Wonka laughs. \"Ok pal, it's alright. But Billy was right for warning you. This room is not open to the general public and you should not be here. How did you even get here in the first place?\"")
    enter()
    display("What do you do?\n1 = tell him about the golden tickets\n2 = don't say anything")
    r = get_r(["1","2"])
    if r == "1":
        display("\"I found the golden tickets that you were advertizing everywhere!\" you say, reaching in your bag and pulling them out.")
        enter()
        bag.remove("golden ticket")
        display("Something changes in Wonka's face. \"Give me those,\" he snaps, ripping them out of your hand. \"Where did you find those?\"")
        enter()
    elif r == "2":
        display("\"I was just stopping by because it's been a while since I've been here,\" you say. \"And then I got lost and ended up here.\"")
        enter()
        display("Wonka nods, but you can see that he is not buying it.")
        enter()
        display("\"Give me your bag.\"")
        enter()
        display("\"What?,\" you hesitate. \"Why?\"")
        enter()
        display("He laughs. \"Has anyone told you that you are a really bad liar?\" He grabs your bag and opens it.")
        enter()
        display("He reaches in and pulls out your wad of collected golden tickets. When he sees them, something changes in his face.")
        enter()
        bag.remove("golden ticket")
        display("\"Where did you get these?!\" he angrily asks, throwing the bag back at you. He holds onto the tickets. You open your mouth to talk again, but it seems that you never regained your ability to speak from before.")
        enter()
    display("\"I- uh, f-found, um, them in-\"")
    enter()
    display("\"SHUT UP\" Wonka booms. \"I put them out in the rooms, but you weren't supposed to find them all. You're smarter than I remember you to be.\"")
    enter()
    display("\"You... remember me?\" You stare at him. He rolls his eyes. \"Yeah, Charlie Bucket, you were the one who tried to take my factory all those years back.\"")
    enter()
    display("Your jaw drops. \"You gave me the factory after I won the golden ticket then, and then you told me that you needed it back.\"")
    enter()
    display("He rolls his eyes. \"Yeah, I came to my senses that nobody (much less a child) would be able to run this factory unless they were me.\"")
    enter()
    display("You stare at him. \"Then why did you have this new challenge? If you're not willing to give up the factory...\"")
    enter()
    display("\"That was just a marketing technique to get more buyers! Nobody was actually supposed to find all of the golden tickets! I thought I made them impossible to find... I should have never put any golden tickets out.\"")
    enter()
    display("You can't believe your ears. This is the man that millions of children are looking up to?")
    enter()
    display("As if reading my mind, Wonka smirks. \"Not what you expected, huh? Well,  that's too bad.\"")
    enter()
    display("Wonka crumples the wad of golden tickets in his hand. \"You won't be needing these anymore,\" he laughs, walking away. \"Billy, get him.\"")
    enter()
    display("The great beast seems to grin at you, baring its glinting, razor-sharp candy teeth. This was talking 'bite-sized candy' to the next leve. You look desperately at Wonka. \"Wha- What are you doing?\"")
    enter()
    display("\"This factory is mine, no matter how hard you try to take it from me,\" he snarls at you. \"You know too much now, anyways.\"")
    enter()
    display("He walks away and the dragon draws closer. You need to act fast if you want to survive! Wonka isn't here to protect you now.")
    enter()
    display("What do you do?\n1 = tempt him with candy\n2 = throw a book at him\n3 = run away")
    r = get_r(["1","2","3"])
    if r == "1":
        if "candy" in bag: #ADD IN CANDY BEFORE
            display("It's a desperate action, but you frantically search your bag for the candy that you found before.")
            enter()
            display("Thankfully, it is still there. You unwrap it and hold it out to the dragon, turning your head away and waiting for the attack.")
            enter()
            display("He never does. You look up to see the dragon sitting like a dog, excitedly panting and sniffing the candy you were holding out to him.")
            enter()
            display("Amazed, you look down at the candy you are holding. Who would have known?")
            enter()
        elif "candy" not in bag:
            display("Sorry, there is no <Candy> in your bag.")
            enter()
            display("The dragon pounces and kills you.")
            enter()
            return "failed"
    elif r == "2":
        display("You grab the first book you can find off the shelf next to you and throw it as hard as you can at the dragon.")
        enter()
        display("The book bounces right off of him and seems to make him even more angry than before.")
        enter()
        display("The dragon pounces and kills you.")
        enter()
        return "failed"
    elif r == "3":
        display("You run as fast as you can towards the door, but the dragon is faster.")
        enter()
        display("He overtakes you and kills you.")
        enter()
        return "failed"
    display("With the candy still held out in front of you, you command the dragon to 'stay' and he obliges.")
    enter()
    display("You slowly make your way over to the desk, where there is a phone next to a stone bust.")
    enter()
    display("Who do you want to call?\n1 = the police\n2 = Grandpa Joe")
    r = get_r(["1","2"])
    if r == "1":
        display("You call the police and tell them everything that happened in the factory.")
        enter()
        display("They come and arrest Willy Wonka. Now that Wonka is gone, the factory is yours!")
        enter()
        display("Congratulations! You have won!")
        enter()
        return "success"
    if r == "2":
        display("You call Grandpa Joe and tell him everything that had happened.")
        enter()
        display("He is shocked, but is glad that you are safe. He says that he will call the police.")
        enter()
        display("Soon, they come and arrest Willy Wonka. Now that Wonka is gone, the factory is yours!")
        enter()
        display("Congratulations! You have won!")
        enter()
        return "success"
#functions for room:

def displayTitle(roomname):
    global title_text
    global canvas
    canvas.itemconfig(title_text,text=roomname)
    canvas.update()

def displayRoomImage(img):
    global room_img
    global canvas
    global screenroom_img
    imgpath = Image.open(os.path.dirname(os.path.abspath(__file__)) + '//' + img)
    resizedimg = imgpath.resize((500,500))
    screenroom_img = ImageTk.PhotoImage(resizedimg)
    canvas.itemconfig(room_img,image=screenroom_img)
    canvas.update()

def enter():             #use to wait for Enter btn, no text input
    global user_entry
    global canvas
    global enter_btn
    user_entry.configure(state='disabled')
    #enter_btn.focus_set()
    waitUntilButtonClicked()

def get_r(accepted_r):
    user_r = inputEnter().lower()
    #enter_btn.focus_set()
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
    global entVar
    global root
    entVar = tk.IntVar()
    enter_btn.wait_variable(entVar)
    print 'button clicked'

def startGame():
    global startBtn
    startVar = tk.IntVar()
    startBtn.wait_variable(startVar)
    print 'start game'

def retFunc(event=None):
    global canvas
    global entVar
    entVar.set(1)

def main():
    global root
    root = tk.Tk()
    app = WonkaApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
