bag = ["key"]
room_solved = False

def display(text):
    print text

def get_r(accepted_r):
    r = raw_input(">> ")
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r

display("Welcome to the Inventing Room! You are standing in the very place where some of Wonka's world-reknown, best-selling candy concoctions came to life!")
display("You stumbled upon a leftover piece of Three Course Dinner Chewing Gum from Violet Beauregarde's unfortunate mishap.")
display("The curious chap that you are, you gave it a try and suddenly you have turned into a blueberry!")
display("You have grown too large to fit through the doorway in which you entered, and the only way to get out is by creating an antidote and returning to normal size.")
display("Luckily, the Inventing Room is stocked with candy syrups, berries, and other ingredients. Have a look around and perhaps you'll find what you need to whip up an antidote! Good luck!")


while (not room_solved):
    display("What would you like to do?\n1 = explore room\n2 = view location descriptions\n3 = view bag\n4 = leave room")
    r = get_r(["1","2","3","4"])
    
    #explore room
    
    if r == "1":
        explore_room = True
        while(explore_room):
            display("Where would you like to go?\n1 = closet\n2 = recipe cabinet\n3 = cauldron\n4 = candy making station\n5 = candy tasting table\n6 = syrup table\n7 = stock pantry\nq = quit")
            r = get_r(["1","2","3","4","5","6","7","q"])
            
            if r == "1":
                if "key" not in bag:
                    display("The closet is locked! You cannot open it.")
                if "key" in bag:
                    display("It looks like the key you found can open the closet. Would you like to open it?")
                    display("1 = yes\n2 = no")
            elif r == "2":
                print "Recipe Cabinet"
            elif r == "3":
                print "Cauldron"
            elif r == "4":
                print "Candy Making Station"
            elif r == "5":
                print "Candy Tasting Table"
            elif r == "6":
                print "Syrup Table"
            elif r == "7":
                print "Stock Pantry"
            elif r == "q":
                explore_room = False
            
    #view location descriptions
    elif r == "2":
        view_loc_desc = True
        while(view_loc_desc):
            display("What would you like to know more about?\n1 = closet\n2 = recipe cabinet\n3 = cauldron\n4 = candy making station\n5 = candy tasting table\n6 = syrup table\n7 = stock pantry\nq = quit")
            r = get_r(["1","2","3","4","5","6","7","q"])
            
            if r == "1":
                display("Cabinet. Holds some secret stuff. Wonka usually keeps it locked for some reason...")
            elif r == "2":
                print "Recipe Cabinet"
            elif r == "3":
                print "Cauldron"
            elif r == "4":
                print "Candy Making Station"
            elif r == "5":
                print "Candy Tasting Table"
            elif r == "6":
                print "Syrup Table"
            elif r == "7":
                print "Stock Pantry"
            elif r == "q":
                view_loc_desc = False

