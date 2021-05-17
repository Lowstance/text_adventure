"""File which contains the character generation class and the relevant
functions
"""
import game_data.characters as chars

class CharacterGenerator:
    """Class which contains the functions relevant to character creation
    """

    @classmethod
    def gen_player(cls):
        return chars.Player("ElenKani", 20, 5)

    @classmethod
    def gen_enemy(cls):
        return chars.Character("Giant rat", 10, 2)
