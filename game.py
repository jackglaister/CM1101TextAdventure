import player, room, os
def GameControl():
    os.system("cls")
    player = CreatePlayer()
    current_room = roomStart()
    while True:
        os.system("cls")
        menu(current_room)	

def CreatePlayer():
    name = input("Please enter your name: ")
    gender = input("Please pick your Gender: Male, Female or Other ")
    if gender.upper() == ("MALE" or "BOY"):
        gender = "male"
    elif gender.upper() == ("FEMALE" or "GIRL"):
        gender = "female"
    else:
        gender = "other"
    return player.player(name,gender)

def roomStart():
    return room.room("the royal kitchen","you are a lowly servant to the Royal Family of Orleasia.",0,0)

def menu(current_room):
    print(current_room.name.upper()+"\n\n"+current_room.description)

GameControl()
