def __init__(self,name,x,y,fl,fr,bl,br):
	self.name=name
	self.number=((x,y))
	self.exits={"forward left":fl, "forward right":fr, "backward left":bl, "backward right":br}