class room():
    def __init__(self, name, description, x, items, exits):	#init class (x and y are location variables)
        self.name=name
        self.description=description
        self.number=x
        self.exits=exits
        self.items=items
