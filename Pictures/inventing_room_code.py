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

