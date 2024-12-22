class FavoriteFood:
    def __init__(self, dish, ingredient1, ingredient2, ingredient3):
        self.__dish = dish
        self.__ingredient1 = ingredient1
        self.__ingredient2 = ingredient2
        self.__ingredient3 = ingredient3
        
    def __str__(self):
        return f"My favorite food is {self.__dish}. Ingredients: {self.__ingredient1}, {self.__ingredient2}, {self.__ingredient3}"

fave1 = FavoriteFood("Pizza", "Cheese", "Tomato sauce", "Pepperoni")
fave2 = FavoriteFood("Pasta", "Spaghetti", "Garlic", "Olive oil")
fave3 = FavoriteFood("Burger", "Beef patty", "Lettuce", "Cheese")

for i in (fave1, fave2, fave3):
    print(i)
