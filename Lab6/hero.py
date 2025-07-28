# hero.py
import random # this is the random module we want to import it to use the choice() fn
from ability import Ability
from armor import Armor

class Hero:
# we want hero to have a default starting health, by default is 100
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
	  # these parameters are passed in so set them as such
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
     # self is taking in another Hero object as a parameter
    def battle(self, opponent): 	
        heros_battle = [self.name, opponent]
        print(f"the winner is {random.choice(heros_battle)}")

    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def add_armor(self, armor):
        self.armors.append(armor)

    def sum_of_attacks(self):
        total = 0
        for ability in self.abilities:
            total = total + ability.attack()
        return total
    
    def defend(self):
        defense = 0
        for armor in self.armors:
            defense = defense + armor.block()
        return defense

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
    my_hero.battle("Superman")
    

