import items, world

class Player(): 
    """Defines all player attributes and actions"""
    def __init__(self):
        self.easy_mode = True
        self.inventory = []
        self.hp = 16
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.equipped_weapon = items.Fists()
        self.available_attacks = []
        self.grab_string = []
#       self.room_text = "This is the default room text."

    def turn_off_easy_mode(self):
        self.easy_mode = False
        print("Easy mode off")

    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        for item in self.inventory:
            print(item.name, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
    """The dx and dy values are jumbled because those are spreadsheet coordinates"""
    def move_north(self):
        self.move(dx=-1, dy=0)
 
    def move_south(self):
        self.move(dx=1, dy=0)
 
    def move_east(self):
        self.move(dx=0, dy=1)
 
    def move_west(self):
        self.move(dx=0, dy=-1)
   
    def equip_weapon(self, weapon):
        """After making equipped_weapon a list, reset list and THEN append weapon to list"""
        self.equipped_weapon = weapon
        
    def equip_dagger(self):
        self.equip_weapon(items.Dagger())
        print("\nYou have equipped your dagger.")
        

    def attack(self, enemy):
        enemy.hp -= self.equipped_weapon.damage
        print("You attack the enemy.")
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            ("{} lives on.".format(enemy.name))
            
    def grab(self, item):
        print(f"\nYou grab the {item[0].name.lower()}.")
        popped_item = item.pop()
        self.inventory.append(popped_item)
        

#Add any more actions here

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
    
    
