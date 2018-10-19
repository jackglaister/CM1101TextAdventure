import player, room
def GameControl():
	player = CreatePlayer()

def CreatePlayer():
	name = input("Please enter your name: ")
	gender = input("Please enter your gender: ")
	return player.player(name,gender)

GameControl()