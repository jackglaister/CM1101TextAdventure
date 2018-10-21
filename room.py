class room():
	def exitsGen(self): #add exits of rooms from a text file for the fixed room positions
		self.exits["forward left"] = room("random name", "random description", x+1, y)
		self.exits["forward right"] = room("random name", "random description", x+2, y)
		self.exits["backward left"] = room("random name", "random description", x-1, y)
		self.exits["backward right"] = room("random name", "random description", x-2, y)
	
	def generate(self, x): 
		exitsGen()

	def __init__(self, name, description, x, y):	#init class (x and y are location variables)
		self.name=name
		self.description=description
		self.number=((x,y))
