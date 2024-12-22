from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name):
        self.name = name
    
    @property
    @abstractmethod 
    def alias(self): 
        pass

class Batman(Character):
    def __init__(self, real_name, alias):
        super().__init__(real_name)
        self._alias = alias
    
    @property
    def alias(self):
        return f"{self.name}, {self._alias}"

Bruce_Wayne = Batman("Bruce Wayne", "Batman") 
print(Bruce_Wayne.alias)
class MLHero:
    def __init__(self, hero_name, role):
        self.hero_name = hero_name
        self.role = role
    def describe(self):
        print(f"{self.hero_name} is a {self.role} hero.")
hero1 = MLHero("Layla","marksman")
hero1.describe()