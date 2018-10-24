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

class oldman(enemy):
    def __init__(self):
        self.attack = ["punch",5]
        self.name = "old man"
        self.health = 40

class oldlady(enemy):
    def __init__(self):
        self.attack = ["ultimatesword",150]
        self.name="old lady"
        self.health = 50

class dragonling(enemy):
    def __init__(self):
        self.name = "dragon"
        self.health = 250
        self.xp = 150
        self.attack = ["wing flap",5]

class soldier(enemy):
    def __init__(self):
        self.name = "Soldier"
        self.health = 100
        self.xp = 100
        self.attack = ["Slash",9]
        #created by edrik
        
class mage(enemy):
    def __init__(self):
        self.name = "mage"
        self.health = 90
        self.xp = 25
        self.attack = ["Beam",7]
        #created by edrik
        
class swordsman(enemy):
    def __init__(self):
        self.name = "Swordsman"
        self.health = 350
        self.xp = 200
        self.attack = ["Slash",15]
        #created by edrik
        
class justicehero(enemy):
    def __init__(self):
        self.name = "Hero of Justice"
        self.health = 600
        self.xp = 250
        self.attack = ["Slash of Justice",20]
        #only appear if player have a negetive karma
        #created by edrik
        
class evilhero(enemy):
    def __init__(self):
        self.name = "Prince of the Underworld"
        self.health = 600
        self.xp = 250
        self.attack = ["Evil beam",20]
        #only appear if player have a bad karma
        #created by edrik
        
class kirill(dragonling):
    def __init__(self):
        self.name = "kirill"
        self.health = 1000
        self.favourite = "caviar"
        self.weakness = "oysters"
        self.attack = ["fire",35]
    def TakeTurn(self, player):
        player.takeDamage(self.attack[1])
        return player

class kid(enemy):
    def __init__(self):
        self.health = 10
        self.name = "kid"
        