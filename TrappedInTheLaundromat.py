import random
active_character = ''

def x():
    x = input("")
    return x

#create a character
class Player:
    """Person whom you will be playing as"""
    def __init__(self, name, description, health, attack, defense, weapon):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon

    #def __str__ == " "

    def introduce(self):
        print(f"""{self.name} Character Profile:
- {self.description}
- Health - {self.health}
- Attack - {self.attack}
- Defense - {self.defense}
- Weapon - {self.weapon}""")

character_list = 'Wallace', 'Julia', 'Franc', 'Jack', 'Ribeye', 'Lamb Chop'

wallace = Player("Wallace","An unapologetically Scottish lumberjack who has many pairs of overalls that must be cleaned thoroughly. Armed with a passion for clean dungarees, this monsterous man will do anything to escape his treacherous laundry run.", 212, 24, 26, "wire hangers")
julia = Player("Julia", "A mild-mannered high-school girl making a living from tutoring a little creature. Is secretly a slayer of men.", 170, 20, 19, "soap flakes w/ 5% concentrate of baking soda")
franc = Player("Franc", "A sensitive soul whose cuff links are made of pig teeth, one from each of his vanquished porkers in his days as a pig wrestler.", 194, 28, 15, "belt made of sausage links from his pig-wrestling days")
jack = Player("Jack", "A CDM who takes no prisoners in his tackles. Only scores from volleys. Washes clothes by hand.", 188, 26, 35, "pet grolar bear that has ferocious teeth")
ribeye = Player("Ribeye", "A product of the Tasmanian outback who rather resembles an echidna at the best of times and the devil at the worst of times.", 175, 23, 18, "soaked towels twisted into lariats")
lamb_chop = Player("Lamb Chop", "A creature of dubious means who is well done...", 200, 17, 22, "army of weasels who hearken to your every word")

has_crocodile = 'has a crocodile'
has_crocodil = False

#game function
def game():

    play = input("Would you like to enter the magical world of the laundromat? Type 'yes' or 'no'.")
    if play == "yes":
        def scene_1():
            print("Introduction:")
            x()
            print("Just when you thought the worst was over with your nightmare in the dryer, the worst is yet to come. For so begins the long, treacherous journey of trying to escape the terrors of the not-so-friendly neighborhood laundromat. Best of luck. The crocodiles bite.")
            x()
            print("Choose a character:")
            print(f"{character_list}")
            x()
            choice = input("Type the name of the character you wish to escape the labyrinth of the laundromat with.")
            if choice == wallace:
                active_character = wallace
            elif choice == julia:
                active_character = julia
            elif choice == franc:
                active_character = franc
            elif choice == jack:
                active_character = jack
            elif choice == ribeye:
                active_character = ribeye
            else:
                active_character = lamb_chop
            print(f"\n{active_character}, your mission is clear. Escape the atrocities of the laundromat.")
            x()
            print("You step out of the dryer, a little fatigued but eager to get out of the laundromat forever. You will NOT be coming back.")
            x()
            print("Collecting your laundry, you turn around, only to see that the entire room has sunken into the ground. You must climb the levels in order to escape.")
            x()
            print(f"Gripping your basket and your {active_character.weapon}, you begin across the room.")
            x()
            print("You begin to think to yourself that this is going to be easy. Some earthquake must have sunken the floor while you had your episode in the dryer, but everything's okay now.")
            x()
            print("You are quite wrong.For just as you lay your foot upon the floor, the tile under it collapses, causing you to trip.")
            x()
            print("You lay on the ground as tiles collapse around and under you, stunned. And to think that this was just a weekly visit to the laundromat!")
            x()
            print("Your basket of laundry falls through the floor as the tiles around it collapse. But that is not your priority right now. It's life or death, and the last thing on your mind is whether your Gucci shirts will ever be seen again.")
            x()
            print("You must decide which tiles are safe. The tiles on the floor are black, grey, and white, but all three colors of tile are collapsing. There must be a sequence.")
            x()
            input_1 = input("Choose a color tile to step on. Type b for black, g for grey, and w for white.")
            tiles_left = 4
            while tiles_left:
                if input_1 == 'b':
                    print("You step hesitantly onto the tile. It holds. You breathe a sign of relief... and then it collapses. You were almost there. Tough luck.")
                    break
                elif input_1 == 'g':
                    print("You confidently jump onto the tile, which promptly collapses. Game over.")
                    break
                elif input_1 == 'w':
                    print("The tile holds.")
                    break
                else:
                    while input_1 not in ('b','w','g'):
                        print("There are only three tile colors. Maybe you're feeling a bit weird after that ordeal in the dryer? Take a minute and try again.")
                        input_1 = input("Choose a color tile to step on. Type b for black, g for grey, and w for white.")
            x()
            print("You stumble across the rest of the tiles. Congratulations! You have passed the first level!")
            x()
            print("The second level is full of shattered washing machines and dryers. You warily glance around, and are shocked to see some wild creatures crawling out of the debris and broken pieces.")
            x()
            print("Among other horrendous beasts, a few crocodiles, snakes, and large tortoises appear out of the wreckage. You freak out.")
            x()
            print("                     '``````^~\"-_`\"-,_ ")
            print("       .-~c~-.                    `~:. ^-. ")
            print("    `~~~-.c    ;                      `:.  `-,     _.-~~^^~:. ")
            print("          `.   ;      _,--~~~~-._       `:.   ~. .~          `. ")
            print("         .` ;'   .:`           `:       `:.   `    _.:-,.    `. ")
            print("        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    ' ")
            print("        :  .' _:'   .-'        `.    :.     .:   .'`.        :    ; ")
            print("        :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ; ")
            print("        `-.__,-~                  ~-.        ,' ':    '.__.`    :' ")
            print("                                     ~--..--'     ':.         .:' ")
            print("                                                     ':..___.:' ")
            x()
            input_2 = input("You are deathly afraid of... a) Rodents of Unusual Size b) Gila Monsters c) Bats (thanks Mr. Stanko)")
            if input_2 == 'a':
                x()
                print("Just your luck. It would be against all copyright laws to put those in this game. Proceed.")
            elif input_2 == 'b':
                x()
                print("HAHA! Not only are Gila Monsters frequent customers of laundromats, they just happen to be in this one! Overcome thy fear or perish!")
            elif input_2 == 'c':
                x()
                print("Hurry and see a healthcare provider. Being in the same room as these bats, no matter what kind, is extremely dangerous. Their rabies may spread. That's a important note, and will be even more important IF you get out.")
            else:
                while input_2 not in ('a', 'b', 'c'):
                    x()
                    print("Unless you wish to disclose all your fears, please choose one of the above letters.")
                    input_2 = input("You are deathly afraid of... a) Rodents of Unusual Size b) Gila Monsters c) Bats (thanks Mr. Stanko)")
            x()
            print("You crawl on top of the nearest washing machine. YOU HAVE THE HIGH GROUND NOW.")
            x()
            print(f"You draw your {active_character.weapon} and prepare to use it. The crocodiles snap at you. They are vicious creatures, and very hungry.")
            x()
            print("              _.'^^'.    ")
            print(" _        _.-' ((@)) '.   ./\/\/\/\/\/\,.---.__\ ")
            print(" ..'o'...-'      ~~~    '~/\/\/\/\/\/\__.---.   `-._ ")
            print(":                         /\/\/\/\,-'              `-.__\ ")
            print("^VvvvvvvvvvvVvVv                                       `-._._._ ")
            print(";^^^^^^^^^^^`         /             `\          /               `-._ ")
            print("```````````````'.`                    `\        (                 `'-._ ")
            print("          .-----'`   /\               `\    )--.______.______._______`/ ")
            print("          (((------'``  `'--------'`(((----' ")

            x()
            print(f"You use your {active_character.weapon} in a threatening manner, but the {active_character.weapon} is quickly devoured by the hungry crocodiles. So much for that.")
            x()
            print("Deciding that you are pretty desperate to get out of this situation, you remember a show you used to watch as a child. What was it called?")
            x()
            print("Ah, yes. The Crocodile Hunter featuring the impeccable Steve Irwin. All the crocodile-hunting skills you learned as a child will surely help you now. Now what is it that could help you in this situation?")
            x()
            input_3 = input("""Which information will you employ from the legendary Crocodile Hunter in order to employ the crocodile as your own?:
                a) Shout 'Crikey!' as loud as humanly possible and leap onto the back of the crocodile
                b) Take out a rotting pig carcass and entice the crocodile to eat, then tie its jaws so it will not bite
                c) Tame it with the soothing touch that only the Crocodile Hunter could give in hopes of winning its affection""")
            if input_3 == 'a':
                x()
                print("The crocodile is momentarily confused, twisting its head to see its familiar friend Steve but once it realizes that you are not he, he opens his jaws wide. Game over.")
                gamecis.exit()
            elif input_3 == 'b':
                x()
                print("The crocodiles see the carcass and remember fondly how Steve used to feed them rotting pig carcasses as well. Driven to tears (real tears), they submit to the pig and allow themselves to be muzzled. You have collected a crocodile.")
                has_crocodile == True
            elif input_3 == 'c':
                x()
                print("The crocodiles roll over once you rub their stomachs. Taking advantage of the opportunity, you run away.")
            else:
                while input_2 not in ('a', 'b', 'c'):
                    x()
                    print("The crocodiles are getting closer. You haven't time to mess around!")
                    input_3 = input("""Which information will you employ from the legendary Crocodile Hunter in order to employ the crocodile as your own?:
                a) Shout 'Crikey!' as loud as humanly possible and leap onto the back of the crocodile
                b) Take out a rotting pig carcass and entice the crocodile to eat, then tie its jaws so it will not bite
                c) Tame it with the soothing touch that only the Crocodile Hunter could give in hopes of winning its affection""")
            x()
            print("You rejoice in your good luck as you pass to the third level.")
            x()
            print("You immediately sneeze. The air is full of something very pungent. You open your eyes to see bubbles everywhere.")
            x()
            print("The earthquake must have disrupted the copious amount of washing liquid and soap flakes throughout the laundromat.You can scarcely see for all the foam floating aroound.")
            x()
            print("You need a way to get out, and fast. Who knows what chemicals are in those soap flakes?")
            x()
            print("As you contemplate what to do next a bolt of lightning strikes the laundromat, causing the lights to flicker.")
            x()
            print("Hovering above the floor appears a familiar face from your ordeal in the dryer: Steve.")
            x()
            input_4 = input("""What do you say to Steve?
                a) Steve? What are you doing here?
                b) You again! I thought I had vanquished thee back in the dryer!
                c) Long time no see old friend. We should meet up like this more often.""")
            if input_4 == 'a':
                x()
                print("""You shout up at Steve, "Steve? what are you doing here?""")

        scene_1()

game()


#https://codereview.stackexchange.com/questions/36768/tiny-text-adventure
#https://asciiart.website//joan/www.geocities.com/SoHo/7373/reptiles.html

