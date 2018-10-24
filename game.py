from player import player
from items import itemDict
import enemy
import room, os
def GameControl():
    os.system("cls")
    current_player = CreatePlayer()
    current_room = roomStart(current_player)
    while True:
        os.system("cls")
        print("Your health is currently: "+str(current_player.health))
        print("Your karma is currently: "+str(current_player.karma)+" and you currently have "+str(current_player.gold)+" gold.")
        if current_room.number % 3 != 0:
            if current_room.name == "Thief's Lair":
                healthTMP = current_player.health+50
                rival = enemy.thief(current_player.health*2, 100)
                current_room, current_player = enterbattle(current_room, current_player, rival)
                current_player.health = healthTMP
                current_room = current_room.next()
            elif current_room == "Bandit attack":
                healthTMP = current_player.health+50
                rival = enemy.bandit(current_player.health*2, 100)
                current_room, current_player = enterbattle(current_room, current_player, enemy)
                current_room = current_room.next()
            elif current_room.name == "Dark Road":
                menu(current_room, current_player)
                while True:
                    answer = input("Do you want to buy the sword, ignore her or attack her for it? \n")
                    answer.split(" ")
                    if len(answer) > 0:
                        if answer[0].lower() == "buy":
                            if current_player.gold < 100:
                                print("You don't have enough gold")
                            else:
                                if current_player.itemsWeight + items["ultimatesword"].weight < 50:
                                    print("You bought an ultimatesword")
                                    current_player.inventory.append(items["ultimatesword"])
                                    current_player.gold -= 100
                                    current_player.karma += 10
                                    current_room = current_room.next()
                                    break
                                else:
                                    print("That will make you too heavy")
                        elif answer[0].lower() == "attack":
                            current_room, current_player = enterbattle(current_room, current_player, enemy)
                            current_room = current_room.next()
                        elif answer[0].lower() == "ignore":
                            print("You move to the next room")
                            current_room = current_room.next()
                        else:
                            print("I didn't understand that")
                    else:
                        print("I didn't understand that")
            elif current_room.name=="The Highway":
                menu(current_room, current_player)
                answer = input("Do you stop to help or ignore him")
                if answer.split(" ")[0] == "stop" or answer.split(" ")[0] == "help":
                    print("You successfully help the old man across the highway, you gain 100 gold and 10 karma")
                    current_player.gold += 100
                    current_player.karma += 10
                    current_room = current_room.next()
                else:
                    print("You leave the old man to postulate crossing the highway on his own")
                    current_player.karma -= 1
                    current_room = current_room.next()
            elif current_room.name=="Merchant's son":
                 menu(current_room, current_player)
                 answer = input("Give directions or leave?")
                 if answer.split(" ")[0].upper() == "GIVE":
                     print("You successfully gave directions to the merchant's son, he gave you 10 gold he got from his father as pocket money")
                     current_player.gold += 10
                     current_room = current_room.next()
                 else:
                     print("You left him on the side of the road to continue his aimless and clueless wondering")
            elif current_room.name=="Wild Animal":
                menu(current_room, current_player)
                answer = input()
                if answer.split(" ")[0].upper() == "WALK":
                    current_player.karma += 10
                    print("You walk around the animal and it continues to happily shield it's cubs, you will gain 10 karma points")
                    current_room = current_room.next()
                else:
                    print("You force the animal out of the way and in doing so, she crushes one of her cubs, you will lose 10 karma points")
                    current_player.karma -= 10
                    current_room = current_room.next()
            elif current_room.name=="Tired Traveller":
                menu(current_room, current_player)
                answer = input()
                if answer.split(" ")[0].upper() == "GIVE":
                    print("The traveller rewards you with 50 gold and thanks you for helping them find the way they need to go")
                    current_player.karma += 5
                    current_player.gold += 50
                    current_room = current_room.next()
                else:
                    print("The exhausted traveller, collapses onto the path behind you and you keep walking on")
                    current_player.karma += 1
                    current_room = current_room.next()
            elif current_room.name=="Lost Kid":
                menu(current_room, current_player)
                answer = input()
                if answer.split(" ")[0].lower() == "feed":
                    if len(answer.split(" ")) < 2:
                        answer = input("feed with what?")
                    else:
                        answer = answer[1:len(answer)]
                    newInventory = []
                    for item in current_player.inventory:
                        if item.name.split(" ")[0].lower() == answer.split(" ")[0].lower():
                            print(item.name+" successfully given to kid, they give you gold and you gain karma")
                            current_player.gold += 5
                            current_player.karma += 5
                        else:
                            newInventory.append(item)
                    if len(newInventory) == len(current_player.inventory):
                        print("unable to give the food")
                    else:
                        current_player.inventory = newInventory
                        current_room = current_room.next()
                else:
                    print("The exhausted kid walked past you in a sloppy way as he is too exhausted to know where to place his feet")
                    current_player.karma -= 1
                    current_room = current_room.next()
            else:
                current_room = current_room.next()
                current_room.number -= 1
        else:
            if current_room.name=="Merchant":
                merchantEncounter(itemDict,current_player,current_room)
            else:
                menu(current_room, current_player)
                current_room, current_player = PrintOptions(current_room, current_player)

def PrintOptions(current_room, current_player):
    printRoomItems(current_room.items)
    printInventoryItems(current_player.inventory)
    print("Your health is currently "+str(current_player.health))
    print("\n What do you wish to do: ")
    printExits(current_room)
    while True:
        answer = input(">")
        answer = answer.split(" ")
        if answer[0].upper() == "GO":
            if len(answer) > 3:
                print("your answer is too long")
            elif len(answer) < 2:
                answer = input("Go where?")
                if current_room.is_valid_exit(answer):
                    current_room = current_room.next()
                    return current_room, current_player
            elif current_room.is_valid_exit(answer[1]):
                current_room = current_room.next()
                return current_room, current_player
        elif answer[0].upper() == "DROP":
            if len(answer) < 2:
                answer = input("drop what?")
                current_player, current_room = drop(answer, current_player, current_room)
            else:
                current_player, current_room = drop(answer[1:len(answer)], current_player, current_room)
        elif answer[0].upper() == "PICK":
            if len(answer) < 3:
                answer = input("pick up what? ")
                current_room, current_player = pickup(answer, current_player, current_room)
            else:
                current_room, current_player = pickup(answer[2:len(answer)], current_player, current_room)
        elif answer[0].upper() == "TAKE":
            if len(answer) < 2:
                answer = input("Take what? ")
                current_room, current_player = pickup(answer, current_player, current_room) 
            else:
                current_room, curernt_player = pickup(answer[1:len(answer)], current_player, current_room)
        elif (answer[0].upper() == "EAT" or answer[0].upper() == "CONSUME"):
            if len(answer) < 2:
                answer = input("Eat what? ")
                current_player = eat(answer, current_player)
            else:
                current_player = eat(answer[1], current_player)
        elif answer[0].upper() == "HELP":
            helpscreen()
        else:
            print("you what????")
            print("Type help if you are stuck for the commands to use")

def eat(answer, current_player):
    newInv = []
    for item in current_player.inventory:
        if answer.upper() == item.name.upper():
            if item.type.upper() == "FOOD":
                current_player.health += item.potency
                current_player.itemsWeight -= item.weight
            else:
                print("I can't eat that!")
                newInv.append(item)
        else:
             newInv.append(item)
    current_player.inventory = newInv
    return current_player

def pickup(answer, current_player, current_room):
    roomitems = []
    for item in current_room.items:
        if item.name.split(" ")[0].upper() == answer[0].upper():
            if current_player.itemsWeight+item.weight < 50:
                current_player.inventory.append(item)
                current_player.itemsWeight += item.weight
                print("Your new weight "+str(current_player.itemsWeight))
            else:
                print("That item would make you too heavy")
        else:
            roomitems.append(item)
    if len(roomitems) == len(current_room.items):
        print("you cannot pick that up")
    else:
        print("successfully picked up "+listToString(answer))
        current_room.items = roomitems
        return current_room, current_player

def drop(answer, current_player, current_room):
    found = False
    inventory = []
    for item in current_player.inventory:
        if answer[0].upper() == item.name.split(" ")[0].upper():
            found = True
            current_room.items.append(item)
            current_player.itemsWeight -= item.weight
        else:
            inventory.append(item)
    if len(inventory) != len(current_player.inventory):
        current_player.inventory = inventory
        print("successfully dropped "+listToString(answer))
        print("Your new weight: "+str(current_player.itemsWeight))
        return current_player, current_room
    else:
        print("you do not have one of those to drop")
        return current_player, current_room

def listToString(listItems):
    string = ""
    for item in listItems:
        string = string+item+" "
    return string

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
    gender = input("Please pick your Gender: Male, Female or Other\n> ")
    if gender.upper() == ("MALE" or "BOY"):
        gender = 1
    elif gender.upper() == ("FEMALE" or "GIRL"):
        gender = 2
    else:
        gender = 3
    return player(name,gender)

def roomStart(current_player):
    return room.room("the royal kitchen","you are a young servant known as "+ current_player.name +".\nYou have fallen ill to a grave illness and have decided to leave\nyour terrible life and seek fame and fortune.",0,[itemDict["bread"],itemDict["fish"],itemDict["honey"],itemDict["chicken"],itemDict["kitchenknife"],itemDict["caviar"],itemDict["oyster"]],["forward","right","left"])

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
        
def merchantEncounter(itemDict,player,current_room):  
    stock = ItemDict
    del stock["caviar"]
    del stock["oyster"]
    del stock["kitchenknife"]
    print("You can buy:\n")
    for i in stock:
        print(i.name,"for",i.value,"gold")
    done = False
    while not done:
        answer = input("\nWhat would you like to do?\n")
        answer = answer.split(" ")
        if answer[0].lower=="leave":
            done=True
            current_room=current_room.next("forward")
        elif answer[0] in ["buy","purchase"]:
            present=False
            for thing in stock:
                if stock[thing].name==answer[1]:
                    item_in_question=stock[thing]
                    present=True
            if not present:
                print("They don't have that here.")
            elif item_in_question.value<player.gold:
                print("Successfully bought a",item_in_question.name)
                player.gold-=item_in_question.value

def enterbattle(current_room, current_player, enemy):
    print("========================================BATTLE========================================")
    while True:
        print("Your health "+str(current_player.health)+"\n Your enemies health: "+str(enemy.health))
        weapons = []
        for item in current_player.inventory:
            if item.type.upper() == "weapon":
                weapons.append(item)
        while True:
            chosenWeapon = input("It is your turn to attack, what do you want to attack with? "+listItems(weapons))
            for item in weapons:
                if chosenWeapon.upper() == item.name.upper():
                    chosenWeapon = item
                    break
            print("I didn't understand that, please try again")
        enemy.TakeDamage(item.potency)
        print("You successfully hit your enemy and their health is now at "+enemy.health)
        if enemy.CheckDeath():
             print("You have dealt your enemy a fatal blow")
             print("You have won the battle, you will advance to the next room and take all the items the enemy has")
             return current_room, current_player
        current_player.HealthDamage(enemy.attack[1])
        print("Your enemy retaliated and reduced your health by "+enemy.attack[1]+" to "+current_player.health+" by using their weapon of "+enemy.attack[0])
        if current_player.CheckDeath():
             print("You lost the battle you will go to the last static room")
             current_room = current_room.LastStatic
             return current_room, current_player

def helpscreen():
    print("HOW TO MOVE \n\ntype go and a direction on your keyboard and hit enter, for example: \ngo forward")
    print("HOW TO TAKE AN ITEM FROM A ROOM \n\ntype 'take' or 'pick up' and then the name of the item and hit enter, for example: \n take bread")
    print("HOW TO DROP AN ITEM FROM YOUR INVENTORY \ntype 'drop' and then the name of the item you wish to drop and press enter, for example: \n drop bread")
    print("HOW TO EAT AN ITEM \ntype 'eat' and then the name of the item in your inventory - you cannot eat straight from the room, for example: \n eat bread")
    print("HOW TO ATTACK \ntype 'hit with' and then the name of the item you want to attack with, for example: hit with kitchen knife")

GameControl()
