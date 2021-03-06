bag = ["Golden Ticket 1","Golden Ticket 2","Golden Ticket 3","Golden Ticket 4","Golden Ticket 5"]
def display(text):
    print text
    
def get_r(accepted_r):
    r = raw_input(">> ").lower()
    while (r not in accepted_r):
        r = raw_input(">> ")
    return r
    
def enter():
    raw_input("Enter>>")

def runFinalRoom():
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
        run_away()
        return "fail"
    elif r == "2":
        stay_still()
    elif r == "3":
        display("\"Help!\" you scream. \"Someone help me!\"")
        enter()
        display("However, your yelling seems to anger the dragon even more and he pounces, killing you.")
        enter()
        return "fail"
    display("\"Billy!\" Wonka goes back to reprimanding his 'little pet.' \"We've been over this before: it's rude to eat guests. I've taught you better!\"")
    enter()
    display("The dragon lowers its gleaming head and Wonka gives it a reassuring pat. \"It's alright, buddy, I know it's tough.\"")
    enter()
    display("You stare in disbelief at the spectacle in front of you. What is going on?!")
    enter()
    display("Wonka meets your shocked eyes and laughs out loud. \"Sorry again, pal. I've had Billy for a few years now and he's still learning. He's just a baby. He's really sweet though, both inside and out.\"")
    enter()
    display("You keep on staring at him. You try to open your mouth and reply, but all that comes out is incomprehensible babble. \"Wh- Wha- Who- How-\"")
    enter()
    display("Wonka laughs. \"Ok pal, it's alright. But Billy was right for warning you. This room is not open to the general public and you should not be here. How did you even get here in the first place?\"")
    enter()
    display("What do you do?\n1 = tell him about the golden tickets\n2 = lie")
    r = get_r(["1","2"])
    if r == "1":
        display("\"I found the golden tickets that you were advertizing everywhere!\" you say, reaching in your bag and pulling them out.")
        enter()
        bag.remove("Golden Ticket 1")
        bag.remove("Golden Ticket 2")
        bag.remove("Golden Ticket 3")
        bag.remove("Golden Ticket 4")
        bag.remove("Golden Ticket 5")
        display("Something changes in Wonka's face. \"Give me those,\" he snaps, ripping them out of your hand. \"Where did you find those?\"")
        enter()
    elif r == "2":
        lie_to_wonka()
    wonka_admits()
    display("What do you do?\n1 = tempt him with candy\n2 = throw a book at him\n3 = run away")
    r = get_r(["1","2","3"])
    if r == "1":
        if "twizzlers" in bag: #ADD IN CANDY BEFORE
            display("It's a desperate action, but you frantically search your bag for the <TWIZZLERS> that you found before in the Squirrel Room.")
            enter()
            display("Thankfully, they are still there. You unwrap them and hold them out to the dragon, turning your head away and waiting for the attack.")
            enter()
            display("He never does. You look up to see the dragon sitting like a dog, excitedly panting and sniffing the candy you were holding out to him.")
            enter()
            display("Amazed, you look down at the candy you are holding. Who would have known?")
            enter()
        elif "candy" not in bag:
            display("Sorry, there are no <TWIZZLERS> in your bag.")
            enter()
            display("The dragon pounces and kills you.")
            enter()
            return "fail"
    elif r == "2":
        display("You grab the first book you can find off the shelf next to you and throw it as hard as you can at the dragon.")
        enter()
        display("The book bounces right off of him and seems to make him even more angry than before.")
        enter()
        display("The dragon pounces and kills you.")
        enter()
        return "fail"
    elif r == "3":
        run_away()
        return "fail"
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

def run_away():
    display("You run as fast as you can towards the door, but the dragon is faster.")
    enter()
    display("He overtakes you and kills you.")
    enter()

def stay_still():
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

def lie_to_wonka():
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
    bag.remove("Golden Ticket 1")
    bag.remove("Golden Ticket 2")
    bag.remove("Golden Ticket 3")
    bag.remove("Golden Ticket 4")
    bag.remove("Golden Ticket 5")
    display("\"Where did you get these?!\" he angrily asks, throwing the bag back at you. He holds onto the tickets. You open your mouth to talk again, but it seems that you never regained your ability to speak from before.")
    enter()
        
def wonka_admits():
    display("\"I- uh, f-found, um, them in-\"")
    enter()
    display("\"SHUT UP\" Wonka booms. \"I put them out in the rooms, but you weren't supposed to find them all. You're smarter than I remember you to be.\"")
    enter()
    display("\"You... remember me?\" You stare at him. He rolls his eyes. \"Yeah, Charlie Bucket, you were the one who tried to take my factory all those years back.\"")
    enter()
    display("Your jaw drops. \"You gave me the factory after I won the golden ticket back then, and a week later you told me that you needed it back.\"")
    enter()
    display("He rolls his eyes. \"Yeah, I came to my senses that nobody (much less a child) would be able to run this factory unless they were me.\"")
    enter()
    display("You stare at him. \"Then why did you have this new challenge? If you're not willing to give up the factory...\"")
    enter()
    display("\"That was just a marketing technique to get more buyers! Nobody was actually supposed to find all of the golden tickets! I thought I made them impossible to find... I should have never put any golden tickets out.\"")
    enter()
    display("You can't believe your ears. This is the man that millions of children are looking up to?")
    enter()
    display("As if reading my mind, Wonka smirks. \"Not what you expected, huh? Well, that's too bad.\"")
    enter()
    display("Wonka crumples the wad of golden tickets in his hand. \"You won't be needing these anymore,\" he laughs, walking away. \"Billy, get him.\"")
    enter()
    display("The great beast seems to grin at you, baring its glinting, razor-sharp candy teeth. This was talking 'bite-sized candy' to the next level. You look desperately at Wonka. \"Wha- What are you doing?\"")
    enter()
    display("\"This factory is mine, no matter how hard you try to take it from me,\" he snarls at you. \"You know too much now, anyways.\"")
    enter()
    display("He walks away and the dragon draws closer. You need to act fast if you want to survive! Wonka isn't here to protect you now.")
    enter()