class enemy():
	def __init__(self, name, xp, health):
		self.name=name
		self.xp = xp
		self.health = health

class dragonenemy(enemy):
	def __init__(self):
		self.name = "dragon"
		self.health = 200
		self.xp = 150