class item():
    def __init__(self,item_id,name,weight,description,value,type):
        self.id=item_id
        self.name=name
        self.weight=weight
        self.description=description
        self.value=value
        self.type=type
        
#item template is item(id,name,weight,description,value)
#eg reference "items.caviar" to call upon it in another file (after importing items)

caviar=item("caviar","caviar",0.1,"salt-cured fish ovum, a rare delicacy",100,"food")
