"""File which contains the state functions of the game
"""


import game_data.character_generator as char_gen

class GameState():
    """Class which contains the state functions of the game
    """

    def __init__(self):
        self.player = char_gen.CharacterGenerator.gen_player()
        self.enemy  = None 

    def start_state(self):
        """Checks the state of the game and spawns enemies if needed

        Returns:
            Character: Enemy spawned
        """
        if self.enemy == None:
            self.enemy = char_gen.CharacterGenerator.gen_enemy() 
            print("You encountered {}".format(self.enemy.get_name()))
        return self.enemy

    def last_state(self):

        if(self.enemy.check_dead()):
            self.enemy = None
            print("The enemy died")
        
        if(self.player.check_dead()):
            print("You died")
            return False
        
        return True


    def get_player(self):
        """returns the game player

        Returns:
            Player: Player of the game
        """
        return self.player
    
    def remove_enemy(self):
        """Removes an enemy from the game
        """
        self.enemy = None