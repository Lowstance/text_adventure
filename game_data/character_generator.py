"""File which contains the character generation class and the relevant
functions
"""
import game_data.characters as chars
import abc
import random as rand

class CharacterGenerator:
    """Class which contains the functions relevant to character creation
    """

    @abc.abstractclassmethod
    def generate(self):
        pass

class PlayerGenerator(CharacterGenerator):
    """Class used to generate the player

    Args:
        CharacterGenerator (class): Character generator class (inherits the
        generate function)
    """

    @classmethod
    def generate(cls):

        name          = input("Give a name: ")
        hit_points    = input("Give hit points: ")
        damage_points = input("Give damage: ")

        return chars.Player(name, int(hit_points), int(damage_points))

class EnemyGenerator(CharacterGenerator):
    """Class used to generate enemies

    Args:
        CharacterGenerator (class): Character generator class (inherits the 
        generate function)
    """
    # Enemy array {name, hit_points, damage_points}
    ENEMY_ARRAY = {"Giant rat"         : [10 , 2],
                   "Giant squid"       : [12 , 3],
                   "Giant pigeon"      : [15 , 4],
                   "Dwarf elephant"    : [13 , 3],
                   "Hostile mirror"    : [7  , 2]
    }

    @classmethod
    def generate(cls):
        
        name, stats = rand.choice(list(cls.ENEMY_ARRAY.items()))
        return chars.Character(name, stats[0], stats[1])
