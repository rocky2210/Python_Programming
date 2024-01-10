# Class

class Car:
    # Constructor
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = True
        
    def start(self):
        if not self.is_running:
            print(f"{self.color} {self.make} {self.model} is starting.")
            self.is_running = True
        else:
            print(f"{self.color} {self.make} {self.model} is already running")

    def stop(self):
        if self.is_running:
            print(f"{self.color} {self.make} {self.model} is stopping.")
            self.is_running = False
        else:
            print(f"{self.color} {self.make} {self.model} is already stopped.")

# Creating instances (objects) of the car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# using methods on the objects
car1.start()
car2.start()
car1.stop()
car2.stop()

"""
    Output:
        Blue Toyota Camry is already running
        Red Honda Civic is already running
        Blue Toyota Camry is stopping.
        Red Honda Civic is stopping.
"""