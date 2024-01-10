# Define a base class for anime characters
class AnimeCharacter:
    def __init__(self,name,series):
        self.name = name
        self.series = series
        
    def introduce(self):
        print(f"I am {self.name} from {self.series}")
        
# Create instances for AnimeCharacter
goku = AnimeCharacter("Goku","Dragon Ball")
asta = AnimeCharacter("Asta","Black clover")

# Introduce the characters
goku.introduce()
asta.introduce()

print("--------------Inheritance--------------")
class Saiyan(AnimeCharacter):
    def __init__(self,name,series,power_level):
        # The super() function is used to give access to methods and properties of a parent or sibling class.
        # The super() function returns an object that represents the parent class.
        super().__init__(name,series)
        self.power_level = power_level
        
    def transform(self):
        print(f"{self.name} is transforming!")
        
class Shinigami(AnimeCharacter):
    def __init__(self, name, series, zanpakuto):
        super().__init__(name, series)
        self.zanpakuto = zanpakuto

    def release_zanpakuto(self):
        print(f"{self.name} is releasing their zanpakuto, {self.zanpakuto}!")

# Create instances of specialized characters
goku = Saiyan("Goku","Dragon Ball", 9000)
ichigo = Shinigami("Ichigo", "Bleach", "Zangetsu")

# Introduce and demostrate abilities 
goku.introduce()
goku.transform()

ichigo.introduce()
ichigo.release_zanpakuto()

"""

I am Goku from Dragon Ball
I am Asta from Black clover
--------------Inheritance--------------
I am Goku from Dragon Ball
Goku is transforming!
I am Ichigo from Bleach
Ichigo is releasing their zanpakuto, Zangetsu!
"""
