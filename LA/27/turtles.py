from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass
    
class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

class Michaelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property
    def alias(self):
        return self.__alias

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property
    def alias(self):
        return self.__alias

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property
    def alias(self):
        return self.__alias


if __name__ == "__main__":
    char5 = Raphael("Splinter", "Sensei")
    print(char5.alias)