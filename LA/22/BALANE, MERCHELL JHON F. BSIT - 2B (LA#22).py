class BirthdayParty:
    def __init__(self, theme, food1, food2, food3, secret_dish):
        self.theme = theme
        self.food1 = food1
        self.food2 = food2
        self.food3 = food3
        self.__secret_dish = secret_dish

    def print_foods(self):
        print(f'''Theme: {self.theme}
Food 1: {self.food1}
Food 2: {self.food2}
Food 3: {self.food3}''')
        self.__print_secret_dish()

    def __print_secret_dish(self):
        print(f"Secret Dish: {self.__secret_dish}")


party1 = BirthdayParty("Victor Magtanggol", "Lechong aso", "Pizza with ipis", "Pinaupong kalabaw", "Ginisang Pagibig")
party2 = BirthdayParty("Two Piece", "Cake ni Nami", "Robin Sticks", "Vivi's Adobayor", "kinalas na buto-buto")
party3 = BirthdayParty("Barbielat", "halululu", "Chicken Adebayor", "sinaganggeng", "pinasarap mo na tinola")

for special_dayz in (party1, party2, party3):
    special_dayz.print_foods()

print() 