# YAPTA

Yet Another Python Text Adventure

YAPTA is an easy-to-use template for creating your very own Python text adventure. The base game mechanics are already implemented so the developer can focus on creating assets for their adventure. Each game mechanic was built with extensibility in mind so that developers can spend their time working on game assets. Only a fundamental knowledge of Python is needed to use this project, although adding your own features may prove more difficult. Documentation is provided for each game mechanic.

## Installation
python-dungeon depends on only one Python package not in the standard library. Use `pip install xlrd` to install the necessary module. It is needed for the program to parse the spreadsheet file.

## How the game works
The player navigates a world using cardinal directions. The player and enemy actions are split up into turns. The player has the ability to pick up items, chiefly weapons and keys, as well as fight enemies. Combat is turnbased. The enemy starts the encounter. The player must determine the enemies weakness(es) as well as how to properly use their weapon to land an attack. The player starts the game in the StartingRoom tile, and must reach the LeaveCaveRoom in order to win. 
### Combat
Special care was put into the combat system to make it unique and intuitive. In order to successfully land an attack on an enemy, the player must combine one of their equipped weapon's techniques with one of the enemies weaknesses. The template for a successful attack looks like this:
'{weapon technique} {enemy weakness}'
So if the player had their dagger equipped and was attacking a giant spider, the attack might look something like this:
'Stab legs'
The challenge for the player is to infer what techniques their weapon has and what weaknesses the enemy has based on their respective descriptions.

## The Player (player.py)
The player is assigned a collection of attributes, including health, inventory, equipped weapon, attacks, and position. `player.py` also contains the various actions the player can perform. `actions.py` provides wrapper classes for these actions.

## Enemies (enemies.py)
This file contains a parent class for all enemies to inherit from. Each enemy has health and damage values, as well as descriptions.

## Items (items.py)
This file contains a parent class for all items to inherit from. A weapon class inherits from the item class as a basis for all of the game's weapons.

## Actions (actions.py)
actions.py contains wrapper classes that game.py uses for the player's actions. Each class points to the action's method in player.py. It also contains a display name for the action, in case listing the available actions for a tile is desired, as well as the input_name, which is what the player needs to type in order to perform the action.

## The Game World (world.py)
The developer can easily design their own levels with the tiles they create by typing the tile's name into a spreadsheet cell. The world.py file parses each cell on the spreadsheet to make an grid for the player to navigate through. The world.py file just needs the path to the spreadsheet file in order to parse it.

## Tiles (tiles.py)
The game world is made of tiles. The player is always on a single tile. A parent class for making lootrooms and enemy rooms is provided. Lootrooms must be supplied an item and enemy rooms must be supplied an enemy. All tiles have an intro text which is generally used to describe to the player what the room looks like. Each room also has a list of available actions that the player can perform, such as moving to adjacent tiles and picking up items. Their are also doors in which the player must have the appropriate key to move through.
