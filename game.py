from player import player
import room, os
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
    print("Your health is currently "+str(current_player.health))
    done = False
    print("\n What do you wish to do: ")
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
        elif answer[0].upper() == "DROP":
            if len(answer) < 2:
                answer = input("drop what?")
                current_player, current_room = drop(answer, current_player, current_room)
            else:
                current_player, current_room = drop(answer[2:len(answer)], current_player, current_room)
        elif answer[0].upper() == "PICK":
            if len(answer) < 3:
                answer = input("pick up what")
                current_room, current_player = pickup(answer, current_player, current_room)
            else:
                current_room, current_player = pickup(answer[2], current_player, current_room)
        elif (answer[0].upper() == "EAT" or answer[0].upper() == "CONSUME"):
            if len(answer) < 2:
                answer = input("Eat what? ")
                current_player = eat(answer, current_player)
            else:
                current_player = eat(answer[1], current_player)
        else:
            print("you what????")

def eat(answer, current_player):
    newInv = []
    for item in current_player.inventory:
        if answer.upper() == item.name.upper():
            if item.type.upper() == "FOOD":
                current_player.health += item.potency
            else:
                print("I can't eat that!")
                newInv.append(item)
        else:
             newInv.append(item)
    current_player.inventory = newInv.append(item)
    return current_player

def pickup(answer, current_player, current_room):
    roomitems = []
    for item in current_room.items:
        if item.name.upper() == answer.upper():
            current_player.inventory.append(item)
        else:
            roomitems.append(item)
    if len(roomitems) == len(current_room.items):
        print("you cannot pick that up")
    else:
        print("successfully picked up "+answer)
        current_room.items = roomitems
        return current_room, current_player

def drop(answer, current_player, current_room):
    found = False
    inventory = []
    for item in current_player.inventory:
        if answer == item.name:
            found = True
            current_room.items.append(item)
        else:
            inventory.append(item.name)
    if (found):
        current_player.inventory = inventory
        return current_player, current_room
        print("successfully dropped "+answer)
    else:
        print("you do not have one of those to drop")
        return current_player, current_room

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
    return player(name,gender)

def roomStart(current_player):
    return room.room("the royal kitchen","you are a young servant known by the name "+ current_player.name +".\nYou have fallen ill to a grave illness and have decided to leave\nyour terrible life and seek fame and fortune.",0,[itemDict["bread"],itemDict["fish"],itemDict["honey"],itemDict["chicken"],itemDict["kitchenknife"]],["forward","right","left"])

def menu(current_room, current_player):
    print(current_room.name.upper()+"\n\n"+current_room.description)

def printRoomItems(itemlist):
    itemslist = listItems(itemlist)
    if itemslist == "":
        print("There are no carryable items in this room")
    else:
        print("You can pick up: "+itemslist+" from here.")

def printInventoryItems(inventory):
    itemslist = listItems(inventory)
    if itemslist == "":
        print("There are no items you can drop")
    else:
        print("You have and can drop "+itemslist)
    edible = []
    for item in inventory:
        if item.type == "food":
            edible.append(item)
    edibleList = listItems(edible)
    if len(edibleList) > 0:
        print("You can also eat: "+edibleList)
    else:
        print("You are carrying no edible items")
def listItems(itemlist):
    itemslist = ""
    for item in itemlist:
        itemslist += item.name+", "
    return itemslist[0:len(itemslist)-2]

def printExits(current_room):
    print("You can: ")
    for exitr in current_room.exits:
        print("Go "+exitr)

GameControl()
