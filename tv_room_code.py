room_solved = False
by_machine = False
oompa_called = False
char_is_dead = False
bag = []

def display(text):
    print text
    
def get_r(accepted_r):
    r = raw_input(">> ").lower()
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r
    
def enter():
    raw_input("Enter>>")

display("Now, you are in the TV Room, where Mike Teavee had his unpleasant incident during the miniaturization display.")
enter()
display("You take a look around the room and observe many strange objects and machinery.")
enter()

while not room_solved: 
    if char_is_dead:
        display("You have failed! Better luck next time!")
        enter()
        break
    
    display("What would you like to do?\n\n1 = explore room\n2 = leave room")
    r = get_r(["1","2"])
    
    #explore room
    if r == "1": 
        display("What would you like to explore?\n\n1 = large piece of machinery in the middle of the room\n2 = table covered in wires\n3 = vintage TV set\nq = quit")
        r = get_r(["1","2","3","q"])
    
        #machinery in center
        if r == "1": 
            by_machine = True
            if "wires" not in bag:
                display("As you approach the intimidating machine, you see a switch on its side.")
                enter()
                display("Curiosity courses through your mind as you get closer to the switch.")
                enter()
                display("You put your finger on the switch and hesitate, remembering the Mike Teavee incident.")
                enter()
                display("The curiosity gets the best of you. You close your eyes and flip the switch.")
                enter()
                display("...")
                enter()
                display("And you wait.")
                enter()
                display("Nothing happens.")
                enter()
                display("Suddenly, you notice that the wires attached to the back of the machine are frayed and broken. No wonder the machine didn't work!")
                enter()
                display("Somewhat relieved, you flip the switch back and decide to explore a different part of the room.")
                enter()
            elif "wires" in bag:
                display("As you get approach the machine, you see broken wires attaching it to the ceiling.")
                enter()
                display("You get closer and also see a red switch on the side of the machine.")
                enter()
                while by_machine:
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
                            display("\"Alright,\" the Oompa Loompa shrugs. \"Your call. Hand over the wires and I'll take care of it.\"")
                            enter()
                            display("You hand over the wires and the Oompa Loompa gets to work. Soon enough, he finishes. \"All done,\" he calls out. \"Now I'm going to go back to that pudding. My lunch break is almost over, so don't bother me again.\"")
                            enter()
                        elif oompa_called:
                            display("\"Hey, little orange man!\" you call out.")
                            enter()
                            display("The Oompa Loompa appears. \"You really have to quit calling me that, kid,\" he grumbles.")
                            enter()
                            display("\"I changed my mind,\" you declare. \"Can you help me wire the machine?\"")
                            enter()
                            #finish this!
                    elif r == "2":
                        print "wire yourself"
                        char_is_dead = True
                        break
                        #you try to wire the machine yourself --> you start out confident but then you accidentally flip the switch and shrink yourself --> Oompa Loompa steps on char and he dead
                    elif r == "3":
                        display("You leave the machine.")
                        by_machine = False
                        break
        #explore table
        elif r == "2":
            if "wires" not in bag:
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
                    display("You whirl around from your bag, guiltily, and come face to face with an anry-looking Oompa Loompa")
                    enter()
                    display("How do you want to respond? You don't think he saw you take the wires, but you are not sure.\n1 = yell back at him\n2 = apologize for taking wires\n3 = pretend that nothing is wrong\n4 = don't say anything")
                    r = (["1","2","3","4"])
                    if r == "1":
                        display("\"What do you think I'm doing?!\" you yell back defiantly. This was the last straw. Being stuck in this factory is messing with your mind.")
                        enter()
                        display("\"It's not my fault that I'm stuck in this stinking factory!")
                        enter()
                        display("\"I'm just trying to find some way to get out of here, and I don't need meddling little orange men poking around in my business!")
                        enter()
                        display("The Oompa Loompa is silent for a second.")
                        enter()
                        display("Eventually, he sighs. \"Look, buddy,\" he sighs. \"I don't want to yell at you as much as you don't want me to. I'm on my lunch break and the last thing I want to be doing is acting like security in the TV room.")
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
                        display("And then he was gone. Your sigh of relief echoes in the silent room. You double check your bag to make sure the <Wires> are still there. They are. You are pretty sure the Oompa Loompa noticed they were missing, but let you slide. That was a close call.")
                        enter()
                    elif r == "2":
                        display("\"Sir, I am so so so sorry,\" you stammer. \"I'm just trying to find some way to get out of this factory so I can go back to my family, and I really don't want to cause any trouble.\"")
                        enter()
                        display("\"I really didn't know that I wasn't supposed to take the wires, and I am so so so sorry. If you need to arrest me, I understand,\" you say with a bowed head.")
                        enter()
                        display("The Oompa Loompa stares at you for a second .")
                        enter()
                        display("Then, out of nowhere, he starts laughing.")
                        enter()
                        display("It starts out with little giggles and ends with him bent over, howling and gasping for air.")
                        enter()
                        display("You just stare at him, confused. Eventually he calms down.")
                        enter()
                        display("\"You humans are so strange,\" he chuckles, turning back to you and wiping tears from his eyes.")
                        enter()
                        display("You keep on staring at him. What just happened?")
                        enter()
                        display("\"Alright look, kid,\" he sighs. \"I didn't even see you take the wires, but I'm technically supposed to report you to the boss for stealing.")
                        enter()
                        display("You look at him with fear in my eyes. You'll never be able to find the golden ticket if you're arrested.")
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
                        print "lie to Oompa Loompa"
                        char_is_dead = True
                        #pretend that nothing is wrong --> Oompa Loompa can tell that you're lying and gets angry (looks in your bag and finds the wires) --> arrests you and game over
                    elif r == "4":
                        print "freeze up out of fear"
                        #freeze up and cannot say anything --> Oompa Loompa feels bad and lets you slide
                elif r == "n":
                    display("Wires are left as they are.")
                    enter()
                    display("You leave the table.")
                    enter()
                else:
                    display("You leave the table.")
                    enter()
            elif "wires" in bag:
                print "choices: 1. call for oompa loompa for help, 2. put wires back, 3. leave table"
                #if oompa loompa called, tells more about room --> if shrink ray tested, explains more about uses --> ask him about shrinking tv (he doesn't know)
        #explore tv set
        elif r == "3":
            display("You approach the old TV set in the corner of the room.")
            enter()
            display("Do you want to turn it on?\n\ny = yes\nn = no\q = quit")
            r = get_r(["y","n","q"])
            if r == "y":
                print "TV on and riddle shown"
                #riddle gives clue that answer is within tv
            if r == "n":
                display("TV is left off.")
                enter()
                display("You leave the TV.")
                enter()
            if r == "q":
                display("You leave the TV.")
                enter()
    #leave room
    elif r == "2":
        print "Go to lobby"
        #go to lobby screen