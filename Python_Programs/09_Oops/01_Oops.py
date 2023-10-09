
#Class
class Car:
    #Constructor
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = True

    def start(self):
        if not self.is_running:
            print("{} {} {} is starting.".format(self.color,self.make,self.model))
            self.is_running = True
        else:
            print("{} {} {} is already running.".format(self.color,self.make,self.model))

    def stop(self):
        if self.is_running:
            print(f"{self.color} {self.make} {self.model} is stopping.")
            self.is_running = False
        else:
            print(f"{self.color} {self.make} {self.model} is already stopped.")

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Using methods on the objects
car1.start()
car2.start()
car1.stop()
car2.stop()