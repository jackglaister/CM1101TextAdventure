from random import randint
import enemy
from puzzles import *
class room():
    def __init__(self, name, description, x, items, exits):	#init class (x and y are location variables)
        self.name=name
        self.description=description
        self.number=x
        self.exits=exits
        self.items=items
        self.enemy=""
    def is_valid_exit(self, desired):
        for exits in self.exits:
            if exits.upper() == desired.upper():
                return True
            else:
                return False
    def next(self,number):
        LastStatic = self
        self = rooms[number]
        try:
            if self == "random":
                roomSelection = randint(0,len(RandRooms)-1)
                self = RandRooms[roomSelection]
                self.number = number
                self.LastStatic = LastStatic
                if roomSelection == 0:
                    self.enemy = oldlady()
                elif roomSelection == 1:
                    self.enemy = oldman()
                elif roomSelection == 2:
                    self.enemy = thief(800, 100)
                elif roomSelection == 3:
                    self.enemy = bandit(300, 100)
                return self
        except:
            self = self
            self.LastStatic = self
            self.number=number
            return self

rooms = [
    "starter room"
    "random",
    "random",
    "random",
    room("Castle Basement","firstPuzzle",5,[],[]),
    "random",
    "random",
    "random",
    room("Puzzle 2","secondPuzzle",9,[],[]),
    "random",
    "random",
    "random",
    room("Merchant","Here is a place where you can buy (almost) anything, use your gold wisely.",13,[],[]),
    "Kirill Encounter",
    "random",
    "random",
    room("Puzzle 3","thirdPuzzle",17,[],[]),
    "random",
    "random",
    "random",
    room("Dragon","You have wondered far into an ominous cave, you heard a roar in the distance and thought you ought to check it out. You have since turned a corner and are faced with a dragon. His name is Kirill and you shall be killed for your trespass",21,[],[])
]

RandRooms = [
    room("Dark Road","An old homeless lady is sat on the edge of a path with a sword. She tells you it is very valuable and was passed down from a long line of ancestors. She is offering it for sale for 100 gold. Do you take it?",0,[],[]),
    room("The Highway","An old man is trying to cross a 4 lane wide highway ahead of you. ",0,[],[]),
    room("Thief's Lair","A thief has approached you and is demanding everything you have. He seems a worthy enemy, you are sure you can take him on.",0,[],[]),
    room("Bandit attack","A bandit is blocking your path ahead, they haven't yet spotted you but one movement could cost your life. Tread carefully.",0,[],[]),
    room("Lost Kid"," A kid is blocking the path in front of you, he appears to be hungry. Do you feed him or leave him? ",0,[],[]),
    room("Merchant's Son"," The merchant's son steps into your path with a clueless look on his face. Do you give him directions or leave him? ",0,[],[]),
    room("Wild Animal"," A wild animal is blocking your path, trying to shield its cubs from you. Do you force the animal out of your way or walk around it? ",0,[],[]),
    room("Tired Traveller"," A wary traveller crosses your path, looking exhausted. Do you give him directions or laugh at him as you walk past? ",0,[],[]),
    room("Castle Basement","Puzzle 1",0,[],[]),
    room("Puzzle 2","puzzle 3",0,[],[]),
    room("Puzzle 3","puzzle 3",0,[],[]),
    room("Dragon","You have wondered far into a dragon's cave, the dragon is called kirill, you can not fight him as you are not strong enough but if you have the secret then you can win the game",0,[],[])
]
