import world, config, tiles
from player import Player


def play():
    """Main gameplay loop"""
    world.load_tiles()
    config.init()
    room = world.tile_exists(config.player.location_x, config.player.location_y)
    print(room.intro_text())
    while config.player.is_alive() and not config.player.victory:
        room = world.tile_exists(config.player.location_x, config.player.location_y)
        room.modify_player(config.player)
        # Check again since the room could have changed the player's state
        if config.player.is_alive() and not config.player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action.display_name)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input in action.input_names:
                    config.player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
