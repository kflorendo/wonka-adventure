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
entVar = ''
backpack_btn = ''
backpack_frame = ''
backpack_text = ''
money = 0
backpack_items = ['0.00']
masterRoot = ''
chocolateFail = False
candyShopSuccess = False
chocolateRoomSuccess = False

#root.configure(background='black')

class WonkaApp:
    def __init__(self, master):
        global masterRoot
        masterRoot = master
        self.master = master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom) 
        mainframe = tk.Frame(masterRoot)
        mainframe.pack()
        self.initializeGameRoom('inventroom.png','hi',mainframe)
        enter()
        #run room functions:
        '''
        runCandyShopIntro()
        runCandyShopRoom()
        display('Oh no! Turns out Willy Wonka has trapped you inside his factory. You must succeed and get the golden ticket in each room to enter the final room.')
        enter()
        display('Maybe you\'ll see him in the final room....')
        enter()'''
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
        displayimg = Label(image = screenroom_img)
        displayimg.image = screenroom_img
        room_img = canvas.create_window(600,100,window = displayimg, anchor = N)

        output_text = canvas.create_text((600,660), anchor = N, fill = 'white', font =('Courier',14),text=displaytext, width = 500)
        error_text = canvas.create_text((600,screenheight-100), anchor = N, fill = 'red', font =('Courier',12),text='')
        canvas.create_line(1200,0,1200,1800, fill="white")
        
        user_entry = Entry(canvas, relief = FLAT, bd = 10)
        user_entry.config(font=("Courier", 14))
        user_entry.pack()
        canvas.create_window(600-100,screenheight-25,window = user_entry, anchor = S)

        enter_btn = Button(canvas, text = "ENTER", font = ('Courier',14),command = retFunc)
        enter_btn.configure(bd = 5)
        enter_btn.pack()
        canvas.create_window(600+100,screenheight-25,window = enter_btn, anchor = S)
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
    global backpack_items
    global backpack_btn
    global canvas
    global backpack_frame
    global backpack_text
    global masterRoot
    displayBackpackString = 'Backpack:\n'
    for item in backpack_items:
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
    gameRunning = True
    lives = 5
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
        if lives <= 0:
            display('You died! Thanks for playing :)')
            gameRunning = False
            enter()
    
def runCandyShopRoomIntro():
    global money
    global candyShopSuccess
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
        backpack_items.append('%.2f'%money)
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
                    backpack_items.append('Laffy Taffy')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('SweeTarts')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('Luminous Lollipop')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('Gobstoppers')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                        backpack_items.append('Golden Ticket 1')
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
                    backpack_items.append('Laffy Taffy')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('SweeTarts')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('Luminous Lollipop')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
                    backpack_items.append('Gobstoppers')
                    if money > 0:
                        backpack_items[0] = ('%.2f'%money)
                    else:
                        backpack_items[0] = '0.00'
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
    if "Luminous Lollipop" in backpack_items:
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
                        backpack_items.append('Golden Ticket 2')
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
                    if 'Golden Ticket 2' in backpack_items:
                        backpack_items.remove('Golden Ticket 2')
                    return 'fail'
                elif health < 0:
                    display('Your health: ' + str(health) + '\\100 \n\nYou\'re health dropped too low!')
                    enter()
                    display('You died. Better luck next time.')
                    enter()
                    if 'Golden Ticket 2' in backpack_items:
                        backpack_items.remove('Golden Ticket 2')
                    return 'fail'
        elif r == 'q':
            return 'fail'
    elif ("Luminous Lollipop" not in backpack_items) and (chocolateFail == False):
        display('Oh no! The room is dark and you can\'t see anything. \n\nIt seems like you\'ll need something to light up the room...')
        enter()
        display('Maybe you can go visit a different room and see if you can find anything. Here\'s 0.50 cents to help you out!\n\nItem added to backpack.')
        money += 0.50
        backpack_items[0] = ('%.2f'%money)
        chocolateFail == True
        enter()
        return
    elif chocolateFail == True:
        display('The room is still dark! You can\'t see anything unless you find something to light up the room. Maybe go back to where it all started...?')
        enter()
        return

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
