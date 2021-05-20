"""File that contains the main gameloop of the game
"""

import game_data.game_state as gstate

def game_loop():
    """Game loop
    """
    state = gstate.GameState()
    player = state.get_player()

    flag = True

    while flag:
        enemy = state.start_state() 
        choice = input("Enter action: ")

        if choice == "attack":
            state.action_attack(player, enemy)

        elif choice == "run":
            player.run()
            state.remove_enemy()
            continue

        elif choice == "heal":
            player.character_heal(5)

        state.action_attack(enemy, player)

        flag = state.last_state()
        if choice == '0':
            break

if __name__ == "__main__":
    print("Welcome")
    game_loop()
