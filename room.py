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
                return true
            else:
                return false
    def next(self, answer):
        x = x + 1
        if (x % 3) == 0:
            ##static room at roomstore
            pass
        else:
            ##random room at roomstore
            pass
