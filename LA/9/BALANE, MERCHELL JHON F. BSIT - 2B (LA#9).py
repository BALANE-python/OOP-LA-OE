class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This car's brand is {self.brand}"

car1 = Car("Mustang")
print(car1)
del car1
print(car1)
