class AnimeCharacter:
    def __init__(self,name,series):
        self.name = name
        self.series = series
        self._health = 100  # Protected attribute
        
    def get_health(self):
        return self._health 
    
    def set_health(self,value):
        if value >= 0:
            self._health = value
            
    def take_damage(self, damage):
        if damage > 0:
            self._health -= damage
            print(f"{self.name} took {damage} damage!")
    
    def heal(self,amount):
        if amount > 0:
            self._health += amount
            print(f"{self.name} healed for {amount} health")

# Create an instance and demostrace encapsulation
goku = AnimeCharacter("Goku","Dragon Ball")
print(f"{goku.name}'s health: {goku.get_health()}") # Access health using getter
goku.set_health(100)  # Access health using setter
goku.take_damage(20)
goku.heal(10)
print(f"{goku.name}'s updated health: {goku.get_health()}")

"""
    Output:
        Goku's health: 100
        Goku took 20 damage!
        Goku healed for 10 health
        Goku's updated health: 90
"""
