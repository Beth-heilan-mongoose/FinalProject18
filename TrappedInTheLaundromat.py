import random
active_character = ''

#create a character
class Player:
    """Person whom you will be playing as"""
    def __init__(self, name, description, health, attack, defense, weapon):
        self.name = name
        self.description = overview
        self.health = hp
        self.attack = atk
        self.defense = defense
        self.weapon = arms

    def introduce(self):
        print(f"""{self.name} Character Profile:
- {self.description}
- Health - {self.health}
- Attack - {self.attack}
- Defense - {self.defense}
- Weapon - {self.weapon}

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
lamb chop = Player("Lamb Chop", "A creature of dubious means who is well done...", 200, 17, 22, "an army of weasels who hearken to his every word")

choice = input("Choose a character.")
    if choice == wallace:
        active_character = wallace
    elif choice == julia:
        active character = julia
    elif choice == franc:
        active character = franc
    elif choice == jack:
        active character = jack
    elif choice == ribeye:
        active character = ribeye
    else:
        active character = lamb chop

play = input
if play.lower() == "yes":
    def scene_1():
        print("Introduction:")
        print("Just when you thought the worst was over with your nightmare in the dryer, the worst is yet to come. For so begins the long, treacherous journey of trying to escape the terrors of the not-so-friendly neighborhood laundromat. Best of luck. The crocodiles bite.")
        choice = input("Choose a character:")
        print character_list
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
        input("Choose a color tile to step on. Type b for black, g for grey, and w for white.")