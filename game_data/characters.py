"""File containing the classes for the characters
"""

class Character:
    """Class used as a template to create characters
    """

    def __init__(self, name, hit_points, damage_points):
        self._name          = name
        self._hit_points    = hit_points
        self._MAX_LIFE      = hit_points
        self._damage_points = damage_points

    def attack(self):
        """Function used to attack

        Returns:
            damage: Damage of the attack
        """

        print(self._name, "attacked")
        return self._damage

    def attacked(self, damage):
        """Function to handle the incoming attack and the results

        Args:
            damage (int): Damage of the attack
        """
        if damage == 1:
            print(self._name, "suffered", damage, "point of damage")
        else:
            print(self._name, "suffered", damage, "points of damage")

        self._hit_points -= damage
        if (self._hit_points < 0):
            self._hit_points = 0

        print("And has", self._hit_points, "left")

    def get_name(self):
        """Get character name

        Returns:
            self._name: Name of the instance
        """
        return self._name

    def check_dead(self):
        """Check if the character is dead

        Returns:
            Bool: Return if the character is dead
        """
        return bool(self._hit_points <= 0)

    def character_heal(self, heal_amount):
        """Heals the character for a specified amount

        Args:
            heal_amount (integer): Heal amount
        """
 
        self._hit_points += heal_amount

        if (self._hit_points > self._MAX_LIFE):
            self._hit_points = self._MAX_LIFE
 

class Player(Character):
    """Class that contains the functions and attributes relevant to the player

    Args:
        Character (Character): Super class Character
    """

    def __init__(self, name, hit_points, damage):
        super().__init__(name, hit_points, damage)
        self.equipment = []

    def run(self):
        """Run from the battle
        """
        print("you ran")

    def equip(self, item):
        """Function to handle the equipment process of an item

        Args:
            item (Item): Item to equip
        """

        self.equipment.append(item)
        self._MAX_LIFE   += item.health_increase
        self._hit_points += item.health_increase
        self._damage     += item.damage_increase
