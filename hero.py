import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        blocked_damage = self.defend()
        damage_taken = damage - blocked_damage
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            if self.is_alive():
                opponent.take_damage(self.attack())

        if self.is_alive():
            self.add_kill()
            opponent.add_death()
            return f"{self.name} won!"
        else:
            self.add_death()
            opponent.add_kill()
            return f"{opponent.name} won!"

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def revive(self):
        self.current_health = self.starting_health
        self.abilities = []
        self.armors = []

