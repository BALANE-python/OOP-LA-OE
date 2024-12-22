class Pizza:
    def __init__(self, name, cheese, ingredients_1, ingredients_2):
        self.name = name
        self._cheese = cheese
        self.__ingredients_1 = ingredients_1
        self.__ingredients_2 = ingredients_2

    def __str__(self):
        return f'''I love {self.name} pizza with {self._cheese} cheese.
ingredients: {self.__ingredients_1}
             {self.__ingredients_2}\n'''
             
    def get_method(self):
        return self.__ingredients_1
   
    def set_method(self, new_ingredients):
        self.__ingredients_1 = new_ingredients

pizza1 = Pizza("Hawaiian", "Mozzarella", "Ham", "Pineapple")
pizza1.set_method("Hotdog")

print(pizza1.get_method())