# Define a base class for anime characters
class AnimeCharacter:
    def __init__(self, name, series):
        self.name = name
        self.series = series

    def introduce(self):
        print(f"I am {self.name} from {self.series}")

# Create instances of AnimeCharacter
goku = AnimeCharacter("Goku", "Dragon Ball")
vegeta = AnimeCharacter("Vegeta", "Dragon Ball")
ichigo = AnimeCharacter("Ichigo", "Bleach")
saitama = AnimeCharacter("Saitama", "One Punch Man")
asta = AnimeCharacter("Asta", "Black Clover")
yuno = AnimeCharacter("Yuno", "Black Clover")
naruto = AnimeCharacter("Naruto", "Naruto")
sasuke = AnimeCharacter("Sasuke", "Naruto")

# Introduce the characters
goku.introduce()
vegeta.introduce()
ichigo.introduce()
saitama.introduce()
asta.introduce()
yuno.introduce()
naruto.introduce()
sasuke.introduce()
