class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def describeToy(self):
        print(f"The pricing range for this {self.name} toy is ${self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
       
Batmobile = Car("Batmobile", "50")
Batmobile.describeToy() 
