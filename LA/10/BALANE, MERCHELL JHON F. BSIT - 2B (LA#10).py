
class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        return f'''
Brand: {self.brand}
Model: {self.model}  
Fuel type: {self.fuel_type}'''

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

Mustang = Car("Ford Mustang", "Dark Horse 2023", "Diesel")
Ducati = Motorcycle("Ducati", "Streetfighter V4", "Diesel")

print(Mustang.describeVehicle())
print(Ducati.describeVehicle())