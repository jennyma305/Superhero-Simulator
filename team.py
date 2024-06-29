class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero_name):
        for hero in self.heroes:
            if hero.name == hero_name:
                self.heroes.remove(hero)
                return
        print(f"No hero named {hero_name} found!")

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        
        if len(self.heroes) > 0:
            avg_kills = total_kills / len(self.heroes)
            avg_deaths = total_deaths / len(self.heroes)
            if avg_deaths > 0:
                kd_ratio = avg_kills / avg_deaths
            else:
                kd_ratio = avg_kills
        else:
            avg_kills = 0
            avg_deaths = 0
            kd_ratio = 0

        print(f"Team {self.name} stats:")
        print(f"  Total Kills: {total_kills}")
        print(f"  Total Deaths: {total_deaths}")
        print(f"  Average K/D Ratio: {kd_ratio:.2f}")

    def attack(self, other_team):
        living_heroes = list(filter(lambda hero: hero.is_alive(), self.heroes))
        living_opponents = list(filter(lambda hero: hero.is_alive(), other_team.heroes))

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            battle_result = hero.fight(opponent)
            print(battle_result)

            living_heroes = list(filter(lambda hero: hero.is_alive(), self.heroes))
            living_opponents = list(filter(lambda hero: hero.is_alive(), other_team.heroes))

    def revive_heroes(self):
        for hero in self.heroes:
            hero.revive()
