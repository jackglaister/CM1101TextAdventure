class room():
    def __init__(self, name, description, x, items, exits):	#init class (x and y are location variables)
        self.name=name
        self.description=description
        self.number=x
        self.exits=exits
        self.items=items
    def is_valid_exit(self, desired):
        for exits in self.exits:
            if exits.upper() == desired.upper():
                return True
            else:
                return False
    def next(self, answer):
        self.number = self.number + 1
        if (self.number % 3) == 0:
            ##static room at roomstore
            pass
        else:
            ##random room at roomstore
            pass
