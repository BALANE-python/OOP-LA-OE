class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper
    
char1 = TekkenCharacter("Kazuya", "Devil Transformation")
@char1.introduce
def character_intro():
    print(f"I am {char1.name} and I can use {char1.ability}")

character_intro()

char2 = TekkenCharacter("Nina", "Stealth Takedown")
@char2.introduce
def character_intro():
    print(f"I am {char2.name} and I can use {char2.ability}")

character_intro()
