"""
    Composition:
        Composition is a "has-a" relationship where one class contains another 
        class as a part of its state. The contained class cannot exist independently 
        of the container class. If the container class is destroyed, all the contained 
        objects are also destroyed.
"""

# Define a base class for anime characters
class AnimeCharacter:
    def __init__(self, name, series):
        self.name = name
        self.series = series
    
    def introduce(self):
        print(f"I am {self.name} from {self.series}")
        
# Create instances of AnimeCharactes
goku = AnimeCharacter("Goku", "Dragon Ball")
saitama = AnimeCharacter("Saitama", "One Punch Man")

# Introduce the characters
goku.introduce()
saitama.introduce()

print("------- Inheritance ------")
class Saiyan(AnimeCharacter):
    def __init__(self, name, series, power_level):
        super().__init__(name, series)
        self.power_level = power_level

    def transform(self):
        print(f"{self.name} is transforming!")


print("------- Polymorphism ------")
def battle(character1, character2):
        print(f"{character1.name} from {character1.series} is battling {character2.name} from {character2.series}")

# Create instances
naruto = AnimeCharacter("Naruto","Naruto")
sasuke = AnimeCharacter("Sasuke","Naruto")

goku = Saiyan("Goku", "Dragon ball", 9000)
vegeta = Saiyan("Vegeta", "Dragon ball", 8000)

# Perform battles with different chacters
battle(naruto,sasuke)
battle(goku,vegeta)

print("------- Composition ------")
class Team:
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
        
    def list_team_members(self):
        print(f"Team Leader: {self.leader.name}")
        print("Team Members:")
        for members in self.members:
            print(f"- {members.name}")
            
# Create a team
team_leader = AnimeCharacter("Naruto", "Naruto")
team_members = [
    AnimeCharacter("Sasuke","Naruto"),
    AnimeCharacter("Sakura","Naruto"),
    AnimeCharacter("Kakashi","Naruto"),
    AnimeCharacter("Minato","Naruto"),
    
]
team = Team(team_leader,team_members)

# List the team members
team.list_team_members()

"""
    Output:
        I am Goku from Dragon Ball
        I am Saitama from One Punch Man
        ------- Inheritance ------
        ------- Polymorphism ------
        Naruto from Naruto is battling Sasuke from Naruto
        Goku from Dragon ball is battling Vegeta from Dragon ball   
        ------- Composition ------
        Team Leader: Naruto
        Team Members:
        - Sasuke
        - Sakura
        - Kakashi
        - Minato
"""