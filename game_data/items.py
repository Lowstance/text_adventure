"""File that contain class definitions for the items of the game
"""

class Item:
    """Class that contains the necessary functionality for the items
    """
    tag = "item"

    def __init__(self, name, value):
        self.name  = name
        self.value = value
 
class Equipment(Item):
    """Class that contains the funcitonality for the game equipment
    """
    tag = "equipment"

    def __init__(self, name, value, health_increase, damage_increase):
        super().__init__(name, value)
        self.health_increase = health_increase
        self.damage_increase = damage_increase

class Consumables(Item):
    """Class that contains the functionality for consumables
    """
    tag = "Consumable"

    def __init__(self, name, value):
        super().__init__(name, value)
