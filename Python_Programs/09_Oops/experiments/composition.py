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

print("------- Inheritance ------")
class Saiyan(AnimeCharacter):
    def __init__(self, name, series, power_level):
        super().__init__(name, series)
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
goku = Saiyan("Goku", "Dragon Ball", 9000)
ichigo = Shinigami("Ichigo", "Bleach", "Zangetsu")

# Introduce and demonstrate abilities
goku.introduce()
goku.transform()

ichigo.introduce()
ichigo.release_zanpakuto()

print("------- Polymorphism ------")
def battle(character1, character2):
    print(f"{character1.name} from {character1.series} is battling {character2.name} from {character2.series}")

# Create instances
naruto = AnimeCharacter("Naruto", "Naruto")
sasuke = AnimeCharacter("Sasuke", "Naruto")

goku = Saiyan("Goku", "Dragon Ball", 9000)
vegeta = Saiyan("Vegeta", "Dragon Ball", 8000)

# Perform battles with different characters
battle(naruto, sasuke)
battle(goku, vegeta)

print("------- Composition ------")
class Team:
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members

    def list_team_members(self):
        print(f"Team Leader: {self.leader.name}")
        print("Team Members:")
        for member in self.members:
            print(f"- {member.name}")

# Create a team
team_leader = AnimeCharacter("Naruto", "Naruto")
team_members = [
    AnimeCharacter("Sasuke", "Naruto"),
    Saiyan("Goku", "Dragon Ball", 9000),
    Shinigami("Ichigo", "Bleach", "Zangetsu"),
]

team = Team(team_leader, team_members)

# List the team members
team.list_team_members()
