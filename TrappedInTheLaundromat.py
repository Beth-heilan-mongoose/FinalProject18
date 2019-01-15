import random
active_character = ''

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

    def introduce(self):
        print(f"""{self.name} Character Profile:
- {self.description}
- Health - {self.health}
- Attack - {self.attack}
- Defense - {self.defense}
- Weapon - {self.weapon}""")

character_list = {
    'champions': {
        ('Wallace', 'Julia', 'Franc', 'Jack', 'Ribeye','Lamb Chop')
    }
}

wallace = Player("Wallace","An unapologetically Scottish lumberjack who has many pairs of overalls that must be cleaned thoroughly. Armed with a passion for clean dungarees, this monsterous man will do anything to escape his treacherous laundry run.", 212, 24, 26, "wire hangers")
julia = Player("Julia", "A mild-mannered high-school girl making a living from tutoring a little creature. Is secretly a slayer of men.", 170, 20, 19, "soap flakes w/ 5% concentrate of baking soda")
franc = Player("Franc", "A sensitive soul whose cuff links are made of pig teeth, one from each of his vanquished porkers in his days as a pig wrestler.", 194, 28, 15, "belt made of sausage links from his pig-wrestling days")
jack = Player("Jack", "A CDM who takes no prisoners in his tackles. Only scores from volleys. Washes clothes by hand.", 188, 26, 35, "pet grolar bear that has ferocious teeth")
ribeye = Player("Ribeye", "A product of the Tasmanian outback who rather resembles an echidna at the best of times and the devil at the worst of times.", 175, 23, 18, "soaked towels twisted into lariats")
lamb_chop = Player("Lamb Chop", "A creature of dubious means who is well done...", 200, 17, 22, "an army of weasels who hearken to his every word")

choice = input("Choose a character.")
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

#game function
def game():

    play = input("Would you like to enter the magical world of the laundromat? Type 'yes' or 'no'.")
if play.lower() == "yes":
    def scene_1():
        print("Introduction:")
        print("Just when you thought the worst was over with your nightmare in the dryer, the worst is yet to come. For so begins the long, treacherous journey of trying to escape the terrors of the not-so-friendly neighborhood laundromat. Best of luck. The crocodiles bite.")
        choice = input("Choose a character:")
        print({character_list})
        x()
        input("Type the name of the character you wish to escape the labyrinth of the laundromat with.")
        x()
        print("[active_character], your mission is clear. Escape the atrocities of the laundromat.")
        x()
        print("You step out of the dryer, a little fatigued but eager to get out of the laundromat forever. You will NOT be coming back.")
        x()
        print("Collecting your laundry, you turn around, only to see that the entire room has sunken into the ground. You must climb the levels in order to escape.")
        x()
        print("Gripping your basket and your {self.weapon}, you begin across the room.")
        x()
        print("The first level passes without event, and you begin to think to yourself that this is going to be easy. Some earthquake must have sunken the floor while you had your episode in the dryer, but everything's okay now.")
        x()
        print("You are quite wrong.For just as you lay your foot upon the second level, the tile under it collapses, causing you to trip.")
        x()
        print("You lay on the ground as tiles collapse around and under you, stunned. And to think that this was just a weekly visit to the laundromat!")
        x()
        print("Your basket of laundry falls through the floor as the tiles around it collapse. But that is not your priority right now. It's life or death, and the last thing on your mind is whether your Gucci shirts will ever be seen again.")
        x()
        print("You must decide which tiles are safe. The tiles on the floor are black, grey, and white, but all three colors of tile are collapsing. There must be a sequence. Choose a color tile.")
        x()
        input_1 = input("Choose a color tile to step on. Type b for black, g for grey, and w for white.")
        tiles_left = 4
        while tiles_left:
            if input_1 == 'b':
                print("You step hesitantly onto the tile. It holds. You breathe a sign of relief... and then it collapses. You were almost there. Tough luck.")
            elif input_1 == 'g':
                print("You confidently jump onto the tile, which promptly collapses. Game over.")
            elif input_1 != ('b','g','w'):
                print("There are only three tile colors. Maybe you're feeling a bit weird after that ordeal in the dryer? Take a minute and try again.")
            else:
                print("The tile holds. Now you must choose the next tile.")
        x()
        print("You stumble across the rest of the tiles. Congratulations! You have passed the second level!")
        x()
        print("The third level is full of shattered washing machines and dryers. You warily glance around, and are shocked to see some wild creatures crawling out of the debris and broken pieces.")
        x()
        print("Among other horrendous beasts, a few crocodiles, snakes, and large tortoises appear out of the wreckage. You freak out.")
        x()
        input_2 = input("You are deathly afraid of... a) Rodents of Unusual Size b) Gila Monsters c) Bats (thanks Mr. Stanko)")
            if input_2 == a:
                print("Just your luck. It would be against all copyright laws to put those in this game. Proceed.")
            elif input_2 == b:
                print("HAHA! Not only are Gila Monsters frequent customers of laundromats, they just happen to be in this one! Overcome thy fear or perish!")
            else input_2 == c:
                print("Hurry and see a healthcare provider. Being in the same room as these bats, no matter what kind, is extremely dangerous. Their rabies may spread. That's a important note, and will be even more important IF you get out.")
        x()
        print("You crawl on top of the nearest washing machine. YOU HAVE THE HIGH GROUND NOW.")
        x()
        print("You draw your {weapon} and prepare to use it. The crocodiles snap at you. They are vicious creatures, and very hungry.")
        x()
        print("You use your {weapon} in a threatening manner, but the {weapon} is quickly devoured by the hungry crocodiles. So much for that.")
        x()
        print("Deciding that you are pretty desperate to get out of this situation, you remember a show you used to watch as a child. What was it called?")
        x()
        print("Ah, yes. The Crocodile Hunter featuring the impeccable Steve Irwin. All the crocodile-hunting skills you learned as a child will surely help you now. Now what is it that could help you in this situation?")
        x()
        input_3 = input("""Which information will you employ from the legendary Crocodile Hunter in order to employ the crocodile as your own?:
            a) Shout 'Crikey!' as loud as humanly possible and leap onto the back of the crocodile
            b) Take out a rotting pig carcass and entice the crocodile to eat, then tie its jaws so it will not bite
            c) Tame it with the soothing touch that only the Crocodile Hunter could give in hopes of winning its affection""")
        if input_3 == a:
            print("The crocodile is momentarily confused, twisting its head to see its familiar friend Steve but once it realizes that you are not he, he opens his jaws wide. Game over.")
        elif input_3 == b:
            print("The crocodiles see the carcass and remember fondly how Steve used to feed them rotting pig carcasses as well. Driven to tears (real tears), they submit to the
        elif input_3 == c:
            print("The crocodiles roll over once you rub their stomachs. Taking advantage of the opportunity, you run away.")


https://codereview.stackexchange.com/questions/36768/tiny-text-adventure

