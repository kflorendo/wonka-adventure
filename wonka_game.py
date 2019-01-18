import Tkinter as tk     # python 2
from Tkinter import *
from PIL import ImageTk,Image
import os
from inventing_room_code import runInventRoom

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
        elif r == '3':
            runInventRoom()
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
        bag.append('%.2f'%money)
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

def runInventRoom():
    global bag
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
                                        return "Failed"
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
                                    return "Succcess"
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
                                        return "Failed"
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
                                        return "Failed"
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
                break



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





