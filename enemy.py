class enemy():
    def __init__(self, name, xp, health):
        self.name=name
        self.xp = xp
        self.health = health
    def TakeDamage(self, damage):
        self.health = self.health - damage
        self.CheckDeath()
    def CheckDeath(self):
        if self.health <= 0:
            self.dead = True
            return True
        else:
            return False

class thief(enemy):
    def __init__(self, health, xp):
        self.name = "thief"
        self.health = health
        self.xp = xp
        self.attack = ["dagger",10]

class bandit(enemy):
    def __init__(self, health, xp):
        self.name = "bandit"
        self.health = health
        self.xp = xp 
        self.attack = ["axe",30]

class oldlady(enemy)
    def __init__(self, health, xp):
        self.attack = ["ultimatesword",150]
        self.name="old lady"
        self.health = 50

class dragonling(enemy):
    def __init__(self):
        self.name = "dragon"
        self.health = 200
        self.xp = 150
        self.attack = ["wing flap",5]

class kirill(dragonling):
    def __init__(self):
        self.name = "kirill"
        self.health = 1000
        self.favourite = "caviar"
        self.weakness = "oysters"
        self.attack = ["fire",10]
    def TakeTurn(self, player):
        player.takeDamage(self.attack[1])
        return player
