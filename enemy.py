class enemy():
	def __init__(self, name, xp, health):
		self.name=name
		self.xp = xp
		self.health = health

class dragonling(enemy):
	def __init__(self):
		self.name = "dragon"
		self.health = 200
		self.xp = 150

class kirill(dragonling):
	def __init__(self):
		self.name = "kirill"
		self.health = 1000
		self.favourite = "caviar"
		self.weakness = "oysters"
