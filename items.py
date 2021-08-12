class Item():
    """The base class for all items."""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description) 


class Weapon(Item):
    """A template for all weapons"""
    def __init__(self, name, description, damage, techniques):
        self.damage = damage
        self.techniques = techniques
        super().__init__(name, description)

    def __str__(self):
        return ""

class Key(Item):
    """The player must have the Key item to walk through doors"""
    def __init__(self):
        super().__init__(name="Key",
                         description="An ornate golden key with red gems encrusted")
