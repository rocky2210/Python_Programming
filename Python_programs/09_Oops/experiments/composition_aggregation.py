class AnimeCharacter:
    def __init__(self, name, series):
        self.name = name
        self.series = series
        
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, character):
        self.members.append(character)

    def list_members(self):
        print(f"Team: {self.team_name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.name} from {member.series}")

# Create instances of AnimeCharacter
naruto = AnimeCharacter("Naruto", "Naruto")
sasuke = AnimeCharacter("Sasuke", "Naruto")
goku = AnimeCharacter("Goku", "Dragon Ball")

# Create a team and add members using composition
team7 = Team("Team 7")
team7.add_member(naruto)
team7.add_member(sasuke)

z_fighters = Team("Z Fighters")
z_fighters.add_member(goku)

# List team members
team7.list_members()
z_fighters.list_members()
