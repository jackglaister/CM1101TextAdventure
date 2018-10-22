class item():
    def __init__(self,item_id,name,weight,description,value,type,potency):
        self.id=item_id         #unique item ID
        self.name=name          #item name
        self.weight=weight      #appropriate weight
        self.description=description    #description of item
        self.value=value        #value of item in gold
        self.type=type          #type e.g. food, weapon, misc
        self.potency=potency    #effectiveness (how much food heals, how much damage a weapon does)

#eg reference "items.caviar" to call upon it in another file (after importing items)
caviar=item("caviar","caviar",0.1,"salt-cured fish ovum, a rare delicacy",100,"food",30)
