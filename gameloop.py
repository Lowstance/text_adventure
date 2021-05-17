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
            damage = player.attack()
            enemy.attacked(damage)

        elif choice == "run":
            player.run()
            state.remove_enemy()
            continue

        damage = enemy.attack()
        player.attacked(damage)

        flag = state.last_state()
        if choice == '0':
            break

if __name__ == "__main__":
    print("Welcome")
    game_loop()
