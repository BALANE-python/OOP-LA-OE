class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper

rias = AnimeCharacter("Rias Gremory", "Power of Destruction")

@rias.introduce
def character_intro():
    print(f"I am {rias.name} and I can use {rias.ability}.")

character_intro()