class room():
	def __init__(self,name,x,y,fl,fr,bl,br):
		self.name=name
		self.number=((x,y))
		self.exits={"forward left":fl, "forward right":fr, "backward left":bl, "backward right":br}

	def __init__(self,name,description,x,y):
		self.description = description
		self.name=name
		self.x=x
		self.y=y
	def exitsGen(self):
		self.exits["forward left"] = room("random name", "random description", x+1, y)
		self.exits["forward right"] = room("random name", "random description", x+2, y)
		self.exits["backward left"] = room("random name", "random description", x-1, y)
		self.exits["backward right"] = room("random name", "random description", x-2, y)
	def generate(self, x)
		exitsGen()
