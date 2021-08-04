import random
import items, enemies, actions, world, config
from player import Player


class MapTile:
    """Parent tile class"""
    config.init()

    def __init__(self, x, y, ):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = []
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                b = config.player.equipped_weapon
                if isinstance(b, items.Dagger):
                    pass
                else:
                    moves.append(actions.EquipDagger())
                    break
        return moves


class StartingRoom(MapTile):
    """The tile that the player first spawns into."""
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = []
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        if config.player.easy_mode is True:
            moves.append(actions.TurnOffEasyMode())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                b = config.player.equipped_weapon
                if isinstance(b, items.Dagger):
                    pass
                else:
                    moves.append(actions.EquipDagger())
                    break
        return moves


class EntranceTile(MapTile):
    """A tile that acts as the introduction to the entire room."""
    def intro_text(self):
        return """You are in a large room that is empty save for a terminal to the north."""

    def modify_player(self, player):
        player.room_text = self.intro_text()


class Door(MapTile):
    """Doors will always face south to north. Anything north of the door is blocked until the door is unlocked"""
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        for a in config.player.inventory:
            if isinstance(a, items.Key):
                return """The door is unlocked. You may walk through."""
                break
        return """The door is locked. Find a key to unlock it."""

    def modify_player(self, player):
        pass

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x - 1, self.y):
            for a in config.player.inventory:
                if isinstance(a, items.Key):
                    moves.append(actions.MoveNorth())
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = []
        # try recreating adjacent moves instead of removing a single adjacent move
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                b = config.player.equipped_weapon
                if isinstance(b, items.Dagger):
                    pass
                else:
                    moves.append(actions.EquipDagger())
                    break
        return moves


class LootRoom(MapTile):
    """Template for all tiles with items"""
    def __init__(self, x, y, item):
        self.item = [item]
        super().__init__(x, y)

    def available_actions(self):
        moves = []
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                b = config.player.equipped_weapon
                if isinstance(b, items.Dagger):
                    pass
                else:
                    moves.append(actions.EquipDagger())
                    break
        if len(self.item) > 0:
            config.player.grab_string = []
            item_string = "Grab {}".format(self.item[0].name.lower())
            print(item_string)
            config.player.grab_string.append(item_string)
            moves.append(actions.GrabItem(item=self.item))

        return moves

    def modify_player(self, player):
        pass


class EnemyRoom(MapTile):
    """Template for all tiles with enemies"""
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            # make this loop repeat infinitely
            random_attack = random.randrange(len(self.enemy.attacks))
            print(self.enemy.attacks[random_attack])

    def available_actions(self):
        moves = []
        if self.enemy.is_alive():
            for a in config.player.equipped_weapon.techniques.values():
                for b in self.enemy.weaknesses.values():
                    string = "{} {}".format(a, b)
                    config.player.available_attacks.append(string)
                    print(string)
                    moves = [actions.Attack(enemy=self.enemy)]
            for a in config.player.inventory:
                if isinstance(a, items.Dagger):
                    b = config.player.equipped_weapon
                    if isinstance(b, items.Dagger):
                        pass
                    else:
                        moves.append(actions.EquipDagger())
                        break
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            for a in config.player.inventory:
                if isinstance(a, items.Dagger):
                    b = config.player.equipped_weapon
                    if isinstance(b, items.Dagger):
                        pass
                    else:
                        moves.append(actions.EquipDagger())
                        break
            return moves


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class RightCorner(MapTile):
    """Same as EmptyCavePath, but different flavor text."""
    def intro_text(self):
        return """
        The corridor turns east.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LeftCorner(MapTile):
    """Same as EmptyCavePath, but different flavor text."""
    def intro_text(self):
        return """
        The corridor turns west.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class HealingFountain(MapTile):
    """Heals the player to full HP."""
    def intro_text(self):
        return """
        You see a glowing fountain before you. The water looks so cool and refreshing that you are filled with determination for whatever lies ahead. You dunk your entire face in and drink as much as you can. Full HP!
        """

    def modify_player(self):
        config.player.hp = 16


class FindKeyTile(LootRoom):
    """This tile contains a key item."""
    def __init__(self, x, y):
        super().__init__(x, y, items.Key())

    def intro_text(self):
        if len(self.item) >= 1:
            return """You notice a golden key on a pedestal."""
        else:
            return """You see a wooden pedestal where the golden key once was."""


class LeaveCaveRoom(MapTile):
    """The player must move to this tile to win the game"""
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
