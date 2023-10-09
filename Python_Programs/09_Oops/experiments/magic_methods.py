class AnimeCharacter:
    def __init__(self, name, series):
        self.name = name
        self.series = series

    def __str__(self):
        return f"{self.name} from {self.series}"

# Create instances and use the __str__ magic method
naruto = AnimeCharacter("Naruto", "Naruto")
sasuke = AnimeCharacter("Sasuke", "Naruto")
goku = AnimeCharacter("Goku", "Dragon Ball")

print(naruto)  # Output: Naruto from Naruto
print(sasuke)  # Output: Sasuke from Naruto
print(goku)    # Output: Goku from Dragon Ball
