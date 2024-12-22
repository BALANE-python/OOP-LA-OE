class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage. {target.name} has {target.health} health left.")

    def special_move(self):
        pass

    def defend(self, attacker):
        damage_taken = max(0, attacker.power - 5)  
        self.health -= damage_taken
        print(f"{self.name} defends against {attacker.name} and takes {damage_taken} damage. {self.name} has {self.health} health left.")


class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.special_used = False  

    def special_move(self):
        if not self.special_used:
            print(f"{self.name} uses Shield Bash!")
            self.power *= 2  
            self.special_used = True  
            return self.power
        else:
            print(f"{self.name} can't use Shield Bash again.")
            return 0  


class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball!")
        return 100  


class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")
        return self.power  


class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50  
        return 0  


# Create characters
warrior = Warrior("Warrior", 150, 20)
mage = Mage("Mage", 100, 15)
archer = Archer("Archer", 100, 10)
monster = Monster("Monster", 300, 25)

characters = [warrior, mage, archer]


for character in characters:
    character.attack(monster)
    special_damage = character.special_move()
    if isinstance(character, Mage):
        monster.health -= special_damage


for character in characters:
    monster.attack(character)


monster.special_move()  


for character in characters + [monster]:
    character.special_move()  


for character in characters + [monster]:
    print(f"{character.name} has {character.health} health left.")
