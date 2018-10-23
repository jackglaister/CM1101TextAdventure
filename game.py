import player, room, os
from items import itemDict
def GameControl():
    os.system("cls")
    current_player = CreatePlayer()
    current_room = roomStart(current_player)
    while True:
        os.system("cls")
        menu(current_room, current_player)
        PrintOptions()

def PrintOptions():
    printRoomItems(current_room.items)
    done = False
    print("\nWhat do you wish to do: ")
    print("GO FORETH to travel to the next room")
    print("pick up and drop and use?") #make another function to say all this like with the demos we had
    while not done:
        answer = input(">")
        if answer.upper() == "GO FORETH":
            #another function to select room and move on 
            done = True
        #elif's for pick up, drop, consume
        else:
            print("you what????")

def CreatePlayer():
    longish = False
    print("Please enter your name: ")
    while not longish:
        name = input(">")
        number = False
        for char in name:
            if not number:
                if char.isdigit():
                    print("No numbers in your name")
                    number = True
        if not number:
            if len(name) <2:
                print("must at least be two characters long")
            elif len(name) >20:
                print("must not exceed twenty characters")
            else:
                longish = True
    os.system("cls")
    gender = input("Please pick your Gender: Male, Female or Other ")
    if gender.upper() == ("MALE" or "BOY"):
        gender = 1
    elif gender.upper() == ("FEMALE" or "GIRL"):
        gender = 2
    else:
        gender = 3
    return player.player(name,gender)

def roomStart(current_player):
    return room.room("the royal kitchen","you are a young servant known by the name "+ current_player.name +".\nYou have fallen ill to a grave illness and have decided to leave\nyour terrible life and seek fame and fortune.",0,[itemDict["bread"],itemDict["fish"],itemDict["honey"],itemDict["chicken"],itemDict["kitchenknife"]],["central","right","left"])

def menu(current_room, current_player):
    print(current_room.name.upper()+"\n\n"+current_room.description)

def printRoomItems(itemlist):
    itemslist = listItems(itemlist)
    if itemslist == "":
        print("there are no carryable items in this room")
    else:
        print("You can pick up: "+itemslist+" from here.")

def listItems(itemlist):
    itemslist = ""
    for item in itemlist:
        itemslist += item.name+", "
    return itemslist
    
GameControl()
