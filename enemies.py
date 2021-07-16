class Enemy:
    """Parent enemy class"""
    def __init__(self, name, hp, damage, weaknesses, attacks):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weaknesses = weaknesses
        self.attacks = attacks
 
    def is_alive(self):
        return self.hp > 0
