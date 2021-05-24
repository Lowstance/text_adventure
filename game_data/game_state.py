"""File which contains the state functions of the game
"""

import game_data.character_generator as char_gen
import game_data.items as item

class GameState():
    """Class which contains the state functions of the game
    """
    available_actions = ["attack", "heal", "equip", "run", "end"]

    def __init__(self):
        self.player = char_gen.PlayerGenerator.generate()
        self.enemy  = None

    def execute_states(state):
        """decorator that executes the start and the end state

        Args:
            state (function): state to execute in the middle
        """

        def wrapper(self, *args, **kwargs):
            self.state_start()
            state(self, *args, **kwargs)
            self.state_last()

        return wrapper

    def state_start(self):
        """Checks the state of the game and spawns enemies if needed
        """
        if self.enemy is None:
            self.enemy = char_gen.EnemyGenerator.generate()
            print("You encountered {}".format(self.enemy.get_name()))

    def state_last(self):
        if self.enemy is not None:
            if self.enemy.check_dead():
                self.enemy = None
                print("The enemy died")

        if self.player.check_dead():
            print("You died")
            return False

        return True

    def action_run(self):
        self.player.run()
        self.check_remove_enemy()

    def action_wait(self):
        pass

    def choose_action(self):
        choice = input("Enter action: ")
        action = Action(self.action_wait)

        while (choice not in self.available_actions):
            print("Please pick a valid choice")
            choice = input("Enter action: ")

        if choice == "attack":
            action = Action(self.phase_damage, self.player, self.enemy)

        elif choice == "run":
            action = Action(self.action_run)

        elif choice == "heal":
            action = Action(self.player.character_heal, 5)

        elif choice == "equip":
            action = Action(self.player.equip, item.Equipment("Bacon", 10, 15, 5))

        elif choice == "end":
            exit()

        return action

    @execute_states
    def state_action(self):
        action = self.choose_action()
        action.execute_action()
        if self.enemy is not None:
            self.phase_damage(self.enemy, self.player)

    def check_remove_enemy(self):
        """Removes an enemy from the game
        """
        self.enemy = None

    def action_attack(self):
        
        pass

    def phase_damage(self, character, target):
        """Function which handles the attack action

        Args:
            character (Character): the character that attacks
            target (Character): the character that is attacked
        """
        damage = character.attack()
        target.attacked(damage)

class Action:
    """Abstract class that executes a given command
    """

    def __init__(self, function, *args):
        self.function  = function
        self.arguments = args

    def execute_action(self):
        self.function(*self.arguments)
