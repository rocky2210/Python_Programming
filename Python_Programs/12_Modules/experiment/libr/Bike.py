from .Automobile import Automobile

class Bike(Automobile):
    #Constructor
    def __init__(self,make,model,regno):
        super().__init__(make,model,regno)