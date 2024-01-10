class AnimeCharacter:
    def __init__(self, name, series):
        self.name = name
        self.series = series
    
    def __str__(self):
        return f"{self.name} from {self.series}"
    
# Create instances and use the __str__ magic method
naruto = AnimeCharacter("Naruto","Naruto")
goku = AnimeCharacter("Goku", "Dragon ball")

print(naruto)
print(goku)

"""
    Output:
        Naruto from Naruto
        Goku from Dragon ball
"""