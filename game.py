import player, room, os
from items import itemDict
def GameControl():
    os.system("cls")
    current_player = CreatePlayer()
    current_room = roomStart(current_player)
    while True:
        os.system("cls")
        menu(current_room, current_player)
        PrintOptions(current_room, current_player)

def PrintOptions(current_room, current_player):
    printRoomItems(current_room.items)
    printInventoryItems(current_player.inventory)
    done = False
    print("\nWhat do you wish to do: ")
    print("pick up and drop and use?") #make another function to say all this like with the demos we had
    printExits(current_room)
    while not done:
        answer = input(">")
        answer = answer.split(" ")
        if answer[0].upper() == "GO":
            if len(answer) > 3:
                print("your answer is too long")
            elif current_room.is_valid_exit(answer[1]):
                current_room = current_room.next(answer[1])
            done = True
        elif answer[0].upper() == "pick":
            if len(answer) < 2:
                answer = input("drop what?")
                drop(answer, current_player)
            else:
                drop(answer[2:len(answer)], current_player, room)
        
        #elif's for pick up, drop, consume
        else:
            print("you what????")

def drop(answer, current_player, room):
    found = False
    inventory = []
    for item in current_player.inventory:
        if answer == item.name:
            found = True
            current_room.items.append(item)
        else:
            inventory.append(item.name)

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
    return room.room("the royal kitchen","you are a young servant known by the name "+ current_player.name +".\nYou have fallen ill to a grave illness and have decided to leave\nyour terrible life and seek fame and fortune.",0,[itemDict["bread"],itemDict["fish"],itemDict["honey"],itemDict["chicken"],itemDict["kitchenknife"]],["forward","right","left"])

def menu(current_room, current_player):
    print(current_room.name.upper()+"\n\n"+current_room.description)

def printRoomItems(itemlist):
    itemslist = listItems(itemlist)
    if itemslist == "":
        print("there are no carryable items in this room")
    else:
        print("You can pick up: "+itemslist+" from here.")

def printInventoryItems(inventory):
    itemslist = listItems(inventory)
    if itemslist == "":
        print("there are no items you can drop")
    else:
        print("you have and can drop "+itemslist)

def listItems(itemlist):
    itemslist = ""
    for item in itemlist:
        itemslist += item.name+", "
    return itemslist


def printExits(current_room):
    print("You can: ")
    for exitr in current_room.exits:
        print("Go "+exitr)

GameControl()
