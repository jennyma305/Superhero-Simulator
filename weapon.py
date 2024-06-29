import random

class Weapon(Ability):
    def attack(self):
        half_max_damage = self.max_damage // 2
        return random.randint(half_max_damage, self.max_damage)