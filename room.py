from random import randint
class room():
    def __init__(self, name, description, x, items, exits):	#init class (x and y are location variables)
        self.name=name
        self.description=description
        self.number=x
        self.exits=exits
        self.items=items
    def is_valid_exit(self, desired):
        for exits in self.exits:
            if exits.upper() == desired.upper():
                return True
            else:
                return False
    def next(self, answer):
        LastStatic = self
        RoomNumber = self.number + 1
        self = rooms[RoomNumber]
        try:
            if self == "random":
                self = RandRooms[randint(0,len(RandRooms)-1)]
                self.number = RoomNumber
                self.LastStatic = LastStatic
                return self
        except:
            self = self
            self.LastStatic = self
            return self

rooms = [
    "starter room"
    "random",
    "random",
    "random",
    room("Castle basement","On the floor of the castle basement appears a puzzle with the following 2,1,18,5, ,18,22,15,17,4 can you determine the item it is hiding?",5,[],[]),
    "random",
    "random",
    "random", 
    room("town centre/merchants","Here is a place where you can buy (almost) anything",9,[],[]),
    "random",
    "random",
    "random",
    room("Dragon","You have wondered far into an ominous cave, you heard a roar in the distance and thought you ought to check it out. You have since turned a corner and are faced with a dragon who told you his name is Kirill and you shall be killed for your trespass",9,[],[])
]

RandRooms = [
    room("Dark Road","An old homeless lady is sat on the edge of a path with a sword she told you was very valuable and was passed down from a long line of ancestors and is offering it for sale for 100 gold",0,[],[]),
    room("The Highway","An old man is trying to cross a 4 lane wide highway ahead of you",0,0,[]),
    room("Thief's Layre","A thief has approached you and is demanding everything you have",0,0,[]),
    room("Bandit attack","A bandit is blocking your path ahead, they haven't yet spotted you but one movement could cost your life",0,0,[])    
]