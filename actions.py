from player import Player
import items
import config


class Action():
    """Parent class for action wrapper classes"""
    def __init__(self, method, display_name, input_names, **kwargs):
        self.method = method
        self.display_name = display_name
        self.input_names = input_names
        self.kwargs = kwargs

    def __str__(self):
        return "{}".format(self.display_name)


"""Create a display_name and an input name for each action"""
class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, display_name='Move north', input_names=['Move north'])


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, display_name='Move south', input_names=['Move south'])


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, display_name='Move east', input_names=['Move east'])


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, display_name='Move west', input_names=['Move west'])


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, display_name='View inventory', input_names=['View inventory'])


class Attack(Action):
    config.init()
    def __init__(self, enemy):
        super().__init__(method=Player.attack, display_name='Attack!', input_names=config.player.available_attacks, enemy=enemy)


class GrabItem(Action):
    config.init()
    def __init__(self, item):
        super().__init__(method=Player.grab, display_name='', input_names=config.player.grab_string, item=item)


class TurnOffEasyMode(Action):
    def __init__(self):
        super().__init__(method=Player.turn_off_easy_mode, display_name='Turn easy mode off', input_names='Turn easy mode off')
