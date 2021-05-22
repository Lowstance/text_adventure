"""File that contains the main gameloop of the game
"""

import game_data.game_state as gstate
import game_data.items as item

def game_loop():
    """Game loop
    """
    state = gstate.GameState()
    flag = True

    while flag:
        state.action_state()


if __name__ == "__main__":
    print("Welcome")
    game_loop()
