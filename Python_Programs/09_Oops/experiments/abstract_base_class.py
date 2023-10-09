from abc import ABC, abstractmethod

class AnimeCharacter(ABC):
    def __init__(self, name, series):
        self.name = name
        self.series = series

    @abstractmethod
    def special_attack(self):
        pass

class Goku(AnimeCharacter):
    def special_attack(self):
        return f"{self.name} uses Kamehameha!"

class Saitama(AnimeCharacter):
    def special_attack(self):
        return f"{self.name} delivers a One Punch!"

# Create instances and call the special_attack method
goku = Goku("Goku", "Dragon Ball")
saitama = Saitama("Saitama", "One Punch Man")

print(goku.special_attack())    # Output: Goku uses Kamehameha!
print(saitama.special_attack()) # Output: Saitama delivers a One Punch!
