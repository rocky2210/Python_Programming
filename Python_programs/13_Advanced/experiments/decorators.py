class AnimeCharacter:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Encapsulated attribute

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be non-negative")

# Create an instance and use property decorators
naruto = AnimeCharacter("Naruto", 16)
print(naruto.age)  # Access age using the getter

naruto.age = 17   # Update age using the setter
print(naruto.age)

# Attempt to set a negative age (raises ValueError)
# naruto.age = -1