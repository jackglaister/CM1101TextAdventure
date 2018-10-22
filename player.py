class player:
	def __init__(self, name, gender):
		self.health = 100
		self.name = name
		self.gender = gender
		self.stamina = 100
		self.xp = 0
		self.inventory = []
	def HealthDamage(self, damage):
		self.health -= damage
	def GainXP(self, damage):
		self.xp = self.health+damage/4
