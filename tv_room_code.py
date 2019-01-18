room_solved = False
questions_done = False
oompa_called = False
machine_wired = False
run_machine = False
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
                            return "fail"
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
                    enter()
                    return "solved"
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
                    enter()
                    return "solved"
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
                        return "fail"
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
        #go to lobby screen
        break