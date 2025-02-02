from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max damage of the weapon? "))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? ")
        max_block = int(input("What is the max block of the armor? "))
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        self.team_one = Team(input("Enter team one name: "))
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        self.team_two = Team(input("Enter team two name: "))
        num_of_team_members = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(f"{self.team_one.name} statistics:")
        self.team_one.stats()
        print("\n")
        print(f"{self.team_two.name} statistics:")
        self.team_two.stats()
        print("\n")

def main():
    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    game_is_running = True

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ").lower()

        if play_again != "y":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

if __name__ == "__main__":
    main()
