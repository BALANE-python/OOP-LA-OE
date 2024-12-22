class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Chirp!")

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

def animal_sounds(animal):
    animal.speak()

dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")
fish = Fish("Fish")

animals = [dog, cat, bird, fish]

for i in animals:
    animal_sounds(i)
