"""
    Static methods belong to a class and don't depend on instance-specific data. Class 
    methods are bound to the class and can access and modify class-level attributes.
"""
class AnimeCharacter:
    total_characters = 0    # Class-level attribute
    
    def __init__(self,name,series):
        self.name = name
        self.series = series
        AnimeCharacter.total_characters +=1
        
    @staticmethod
    def total_count():
        return AnimeCharacter.total_characters
    
    @classmethod
    def print_intro(cls):
        print(f"Welcome to the world of anime characters! we have {cls.total_count()} characters.")

# Create instances and use static and class methods
naruto = AnimeCharacter("Naruto","Naruto")
goku = AnimeCharacter("Goku","Dragon ball")

AnimeCharacter.print_intro()
print(f"Total characters created: {AnimeCharacter.total_count()}")

"""
    Output:
        Welcome to the world of anime characters! we have 2 characters.
        Total characters created: 2
"""