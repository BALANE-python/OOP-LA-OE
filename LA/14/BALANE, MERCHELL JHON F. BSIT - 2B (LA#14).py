class Spiderman:
    def __init__(self, name, age):
        self.name = name.lower()
        self.age = age
        
    def describeSpiderman(self):
        print(f"{self.name} is {self.age} years old.")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle


tobey = Tobey("Tobey", 29, "Spiderman 1")
andrew = Andrew("Andrew", 28, "Spiderman 2")
tom = Tom("Tom", 24, "Spiderman 3")


print(f"{tobey.name.upper()}, {tobey.movieTitle}")
print(f"{andrew.name.upper()}, {andrew.movieTitle}")
print(f"{tom.name.upper()}, {tom.movieTitle}")
