"""File containing the classes for the characters
"""

class Character:
    """Class used as a template to create characters
    """

    def __init__(self, name, hit_points, damage):
        self.__name       = name
        self.__hit_points = hit_points
        self.__damage     = damage

    def attack(self):
        """Function used to attack

        Returns:
            damage: Damage of the attack
        """

        print(self.__name, " attacked")
        return self.__damage

    def attacked(self, damage):
        """Function to handle the incoming attack and the results

        Args:
            damage (int): Damage of the attack
        """
        if damage == 1:
            print(self.__name, "suffered", damage, "point of damage")
        else:
            print(self.__name, "suffered", damage, "points of damage")

        self.__hit_points -= damage

        print("And has", self.__hit_points, "left")

    def get_name(self):
        """Get character name

        Returns:
            self.__name: Name of the instance
        """
        return self.__name

    def check_dead(self):
        """Check if the character is dead

        Returns:
            Bool: Return if the character is dead
        """
        return bool(self.__hit_points <= 0)


class Player(Character):
    """Class that contains the functions and attributes relevant to the player

    Args:
        Character (Character): Super class Character
    """

    def run(self):
        """Run from the battle
        """
        print("you ran")
