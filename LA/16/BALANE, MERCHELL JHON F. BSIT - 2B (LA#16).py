class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!")
    def info(self):
        print(self.brand, self.model)

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

washingMachine = WashingMachine("Miele", "W1 TwinDos")
refrigerator = Refrigerator("Sub-Zero", "BI-36U")
microwave = Microwave("Wolf", "Microwave Drawer")

for appliance in (washingMachine, refrigerator, microwave):
    appliance.operate()
    appliance.info()
