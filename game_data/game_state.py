"""File which contains the state functions of the game
"""

import game_data.character_generator as char_gen
import game_data.items as item

class GameState():
    """Class which contains the state functions of the game
    """

    def __init__(self):
        self.player = char_gen.PlayerGenerator.generate()
        self.enemy  = None

    def execute_states(state):
        """decorator that executes the start and the end state

        Args:
            state (function): state to execute in the middle
        """

        def wrapper(self, *args, **kwargs):
            self.start_state()
            state(self, *args, **kwargs)
            self.last_state()

        return wrapper

    def start_state(self):
        """Checks the state of the game and spawns enemies if needed
        """
        if self.enemy is None:
            self.enemy = char_gen.EnemyGenerator.generate()
            print("You encountered {}".format(self.enemy.get_name()))

    def last_state(self):
        if self.enemy is not None:
            if self.enemy.check_dead():
                self.enemy = None
                print("The enemy died")

        if self.player.check_dead():
            print("You died")
            return False

        return True

    def state_run(self):
        self.player.run()
        self.remove_enemy()

    def state_wait(self):
        pass

    def choose_action(self):
        choice = input("Enter action: ")
        action = Action(self.state_wait)

        if choice == "attack":
            #state.action_attack(player, enemy)
            action = Action(self.action_attack, self.player, self.enemy)

        elif choice == "run":
            #player.run()
            action = Action(self.state_run)
            #state.remove_enemy()
            #continue

        elif choice == "heal":
            #player.character_heal(5)
            action = Action(self.player.character_heal, 5)

        elif choice == "equip":
            action = Action(self.player.equip, item.Equipment("Bacon", 10, 15, 5))
            #player.equip(item.Equipment("Bacon armor", 10, 15, 5))

        #state.action_attack(enemy, player)

        return action

    @execute_states
    def action_state(self):
        action = self.choose_action()
        action.execute_action()
        self.action_attack(self.enemy, self.player)

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

    def action_attack(self, character, target):
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
