# Define a base class for anime characters
class AnimeCharacter:
    def __init__(self,name,series):
        self.name = name
        self.series = series
        
    def introduce(self):
        print(f"I am {self.name} from {self.series}")
        
# Create instances of Animecharacters
goku = AnimeCharacter("Goku", "Dragon Ball")
naruto = AnimeCharacter("Naruto", "Naruto")
luffy = AnimeCharacter("Luffy","One piece")
saitama = AnimeCharacter("Saitama", "One Punch Man")
asta = AnimeCharacter("Asta", "Black Clover")

# Introduce the charactes
goku.introduce()
naruto.introduce()
luffy.introduce()
saitama.introduce()
asta.introduce()

"""
I am Goku from Dragon Ball
I am Naruto from Naruto
I am Luffy from One piece
I am Saitama from One Punch Man
I am Asta from Black Clover
"""
