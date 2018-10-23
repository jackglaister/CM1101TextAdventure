import player, room, os
def GameControl():
    os.system("cls")
    current_player = CreatePlayer()
    current_room = roomStart(current_player)
    while True:
        done = False
        os.system("cls")
        menu(current_room, current_player)
        print("\nWhat do you wish to do: ")
        print("GO FORETH to travel to the next room")
        print("pick up and drop and use?") #make another function to say all this like with the demos we had
        while not done:
            answer = input(">")
            if answer.upper() == "GO FORETH":
                done = True
            else:
                print("you what????")

def CreatePlayer():
    name = input("Please enter your name: ")
    gender = input("Please pick your Gender: Male, Female or Other ")
    if gender.upper() == ("MALE" or "BOY"):
        gender = 1
    elif gender.upper() == ("FEMALE" or "GIRL"):
        gender = 2
    else:
        gender = 3
    return player.player(name,gender)

def roomStart(current_player):
    return room.room("the royal kitchen","you are a young servant known by the name "+ current_player.name +".\nYou have fallen ill to a grave illness and have decided to leave\nyour terrible life and seek fame and fortune.",0,0)

def menu(current_room, current_player):
    print(current_room.name.upper()+"\n\n"+current_room.description)

GameControl()
