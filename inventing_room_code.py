bag = ["key", "blueberry extract", "fruity tooty lollipop", "purple taffy"]

cabinet_contents = ["secret formula", "deflation gumdrops"]

candy_recipe_folder = ["fruity tooty lollipop recipe","groovy grape taffy recipe","twisty tangy twizzlers recipe"]
chocolate_recipe_folder = ["golden ticket"]
antidote_recipe_folder = ["blueberry antidote recipe piece 1"]

cauldron = []
cauldron_attempts_left = 2
antidote_ingredients_list = ["blueberry extract", "deflation gumdrops", "fruity tooty lollipop", "purple taffy", "secret formula"]

room_solved = False
char_is_dead = False

def display(text):
    print text

def get_r(accepted_r):
    r = raw_input(">> ").lower()
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r

def enter():
    raw_input("Enter>>")

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
    
    display("What would you like to do?\n\n1 = explore room\n2 = view location descriptions\n3 = view bag\n4 = leave room")
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
                                    break
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
                    if r == "q":
                        explore_cauldron = False
            elif r == "4":
                print "Candy Making Station"
            elif r == "5":
                print "Candy Tasting Table"
            elif r == "6":
                print "Syrup Table"
            elif r == "7":
                explore_pantry = True
                while(explore_pantry):
                    display("Which cabinet would you like to look in?\n1 = extracts\n2 = berries\nq = quit")
                    r = get_r(["1","2","q"])
                    
                    #extract cabinet
                    if r == "1":
                        if "decipher spray" in bag:
                            print "cool!"
                        else:
                            display("The words on the extract bottle labels appear to be faded. You look on the cabinet door and a note is posted:")
                            enter()
                            display("ATTENTION\nThis cabinet contains extract bottles. If they are not polished every 3 weeks, the labels may begin to fade.\nA decipher spray crafted with jolly ranchers can be used to spray bag.")
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

