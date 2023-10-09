class AnimeCharacter:
    def __init__(self, name, series, power_level):
        self.name = name
        self.series = series
        self.power_level = power_level

    def __str__(self):
        return f"{self.name} from {self.series} (Power Level: {self.power_level})"

    def __gt__(self, other):
        return self.power_level > other.power_level

# Create instances of AnimeCharacter
goku = AnimeCharacter("Goku", "Dragon Ball", 9000)
saitama = AnimeCharacter("Saitama", "One Punch Man", 10000)

# Use the > operator for power level comparison
print(goku > saitama)  # Output: False (Goku's power level is not greater)
#haha but goku is stronger than saitama