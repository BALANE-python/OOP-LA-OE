class FavoriteFood:
    def __init__(self, dish, ingredient1, ingredient2, ingredient3):
        self.__dish = dish
        self.ingredient1 = ingredient1
        self._ingredient2 = ingredient2
        self.__ingredient3 = ingredient3

    def __str__(self):
        return f"My favorite food is {self.__dish}. Ingredients: {self.ingredient1}, {self._ingredient2}, {self.__ingredient3}"
    
    def get_ingredient3(self):
        return self.__ingredient3

fave1 = FavoriteFood("Fried Chicken", "Chicken", "Flour", "Cooking oil")


print(fave1.get_ingredient3())  



