room_solved = False
by_machine = False
char_is_dead = False
bag = ["wires"]

def display(text):
    print text
    
def get_r(accepted_r):
    r = raw_input(">> ")
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r
    
def enter():
    raw_input("Enter>>")

display("Now, you are in the TV Room, where Mike Teavee had his unpleasant incident during the miniaturization display.")
display("You take a look around the room and observe many strange objects and machinery.")

while not room_solved: 
    if char_is_dead:
        display("You have failed! Better luck next time!")
        enter()
        break
    
    display("What would you like to do?\n1 = explore room\n2 = view bag\n3 = leave room")
    r = get_r(["1","2","3"])
    
    if r == "1":
        display("What would you like to explore?\n1 = large piece of machinery in the middle of the room\n2 = table covered in wires\n3 = vintage TV set\nq = quit")
        r = get_r(["1","2","3","q"])
    
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
                display("Suddenly, you notice the broken wires attached to the back of the machine. No wonder the machine didn't work!")
                enter()
                display("Somewhat relieved, you flip the switch back and decide to explore a different part of the room.")
                enter()
            elif "wires" in bag:
                display("As you get approach the machine, you notice some broken wires attaching it to the ceiling.")
                enter()
                display("You get closer and also see a red switch on the side of the machine.")
                enter()
                while by_machine:
                    display("What would you like to do?\n1 = get Oompa Loompas to help you rewire machine\n2 = try to rewire machine yourself\n3 = try to run the machine as it is\n4 = leave and explore something else")
                    r = get_r(["1","2","3","4"])
                    if r == "1":
                        print "Oompa Loompas help you"
                        #get Oompa Loompas to help you --> they are grumpy and complain a lot but help you successfully wire it
                    elif r == "2":
                        print "wire yourself"
                        char_is_dead = True
                        break
                        #you try to wire the machine yourself --> you start out confident but then you accidentally flip the switch and shrink yourself --> Oompa Loompa steps on char and he dead
                    elif r == "3":
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
                        display("Suddenly, you notice the broken wires attached to the back of the machine. No wonder the machine didn't work!")
                        enter()
                        display("Somewhat relieved, you flip the switch back and decide to try something else.")
                        enter()
                    elif r == "4":
                        display("You leave the machine.")
                        by_machine = False
                        break
            