bag = ["key"]

cabinet_contents = ["secret formula", "deflation gumdrops"]

candy_recipe_folder = ["fruity tooty lollipop recipe","groovy grape taffy recipe","twisty tangy twizzlers recipe"]
room_solved = False
char_is_dead = False

def display(text):
    print text

def get_r(accepted_r):
    r = raw_input(">> ")
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r

def enter():
    raw_input("Enter>>")

def add_remove_item(item, add_loc, remove_loc):
    

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
    
    if char_is_dead:
        display("You have failed! Better luck next time!")
        enter()
        break
    
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
                    enter()
                if "key" in bag:
                    display("It looks like the key you found can open the closet. Would you like to open it?\ny = yes\nn = no")
                    r = get_r(["y","n"])
                    if r == "y":
                        if "secret formula" in cabinet_contents:
                            display("There is a small vile with a mysterious blue liquid. What would you like to do?\n1 = put in bag\n2 = drink the liquid\n3 = leave in closet")
                            r = get_r(["1","2","3"])
                            if r == "1":
                                bag.append("secret formula")
                                cabinet_contents.remove("secret formula")
                                display("You have added <SECRET FORMULA> to your bag.")
                                enter()
                            if r == "2":
                                display("The liquid is too strong on its own! Are you sure you would like to drink it?\ny = yes\nn = no")
                                r = get_r(["y","n"])
                                if r == "y":
                                    display("The liquid was too strong to digest. You have lost a life!")
                                    char_is_dead = True
                                    enter()
                                    break
                        if "deflation gumdrops" in cabinet_contents:
                            display("You have found <DEFLATION GUMDROPS>! Would you like to put them in your bag?\ny = yes\nn = no")
                            r = get_r(["y","n"])
                            if r == "y":
                                bag.append("deflation gumdrops")
                                cabinet_contents.remove("deflation gumdrops")
                                display("You have added <DEFLATION GUMDROPS> to your bag.")
                                enter()
                        if len(cabinet_contents) == 0:
                            display("The cabinet is empty.")
                            enter()
            elif r == "2":
                display("This is the recipe cabinet. Add a recipe to your bag to view it. Which folder would you like to look in?\n1 = candy\n2 = chocolates\n3 = antidotes\n4 = none")
                r = get_r(["1","2","3"])
                if r == "1":
                    if "fruity tooty lollipop" in candy_recipe_folder:
                        display("Would you like to add the <FRUIT TOOTY LOLLIPOP RECIPE> to your bag?\ny = yes\nn = no")
                        r = get_r(["y","n"])
                        if r == "y":
                            bag.append("fruity tooty lollipop recipe")
                            candy_recipe_folder.remove("fruity tooty lollipop recipe")
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
    
    elif r == "4":
        display("Your progress will not be saved and items you have picked up in this room will not remain in your bag. Would you like to continue?\ny = yes\nn = no")
        r = get_r(["y","n"])
        if r == "y":
            display("You have left the room.")
            enter()
            break

