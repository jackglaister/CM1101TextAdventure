import player, room
def GameControl():
	player = CreatePlayer()
	current_room = starterRoom()

def CreatePlayer():
	name = input("Please enter your name: ")
	gender = input("Please enter your gender: ")
	return player.player(name,gender)

def starterRoom():
	return room.room("start","description",0,0)

def menu(current_room):
	print(current_room.name+"\n"+current_room.description)

GameControl()