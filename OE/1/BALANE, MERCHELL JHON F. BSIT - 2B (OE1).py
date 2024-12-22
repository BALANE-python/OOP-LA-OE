class Hero:
    def __init__(self, name, role, damage_type, lane):
        self.name = name
        self.role = role
        self.damage_type = damage_type
        self.lane = lane

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Damage Type: {self.damage_type}, Lane: {self.lane}"

class MobileLegendsDreamTeam:
    def __init__(self):
        self.heroes = [
            Hero("Edith", "Tank/Marksman", "Physical Damage", "EXP Lane"),
            Hero("Ruby", "Fighter", "Physical Damage", "Gold Lane"),
            Hero("Julian", "Fighter/Mage", "Magical  Damage", "Jungler"),
            Hero("Aurora", "Mage", "Magical Damage", "Mid Lane"),
            Hero("Floryn", "Support", "Magical Damage", "Roaming")
        ]

    def print_team_description(self):
        print("Mobile Legends Dream Team:")
        for hero in self.heroes:
            print(hero)


dream_team = MobileLegendsDreamTeam()
dream_team.print_team_description()
