class player:
    def __init__(self, name, gender):
        self.health = 100
        self.name = name
        self.gender = gender #1 is male, 2 is female, 3 is other
        self.stamina = 100
        self.xp = 0
        self.inventory = []
        self.itemsWeight = 0
        self.gold = 200
        self.karma = 0
    def HealthDamage(self, damage):
        self.health -= damage
    def GainXP(self, damage):
        self.xp = self.xp+damage/4
    def CheckDeath(self, damage):
        if self.health < 0:
            return True
        else:
            return False
