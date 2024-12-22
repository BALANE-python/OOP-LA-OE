class MLHero:
    def __init__(self, hero_name, role):
        self.hero_name = hero_name
        self.role = role

    def describe(self):
        print(f"{self.hero_name} is a {self.role} hero.")

    def __str__(self):
        return f"{self.hero_name} is a {self.role} hero."
    
    def printmethod(self): 
        print(self)

hero1 = MLHero("Granger","marksman")
hero1.printmethod()