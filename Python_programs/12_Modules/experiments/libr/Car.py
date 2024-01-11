from .Automobile import Automobile
class Car(Automobile):
    # Class attribute
    type = "BMW"
    
    # Constructor
    def __init__(self,make,model,regno):
        # Instance attributes
        super().__init__(make,model,regno)
        self.batt = 0
        if self.type == "BMW":
            self.breakpow = "100%"
        elif self.type == "benz":
            self.breakpow = "75%"
            
    @classmethod 
    def build_from_automobile(cls,e: Automobile):
        c = cls(e.carmake,e.carmodel,e.carregno)
        return c
    
    def start(self):
        print(f"Burmmmm.....{self.carmake} {self.carmodel} {self.carregno } is ready to drive")
        
    
    def get_battery(self):
        print(f"Battery : {self.batt}%")
        
    @classmethod
    def get_type(cls):
        g = cls("Marton",2342,"TNwerwer")
        g.start()
        return g
    
    @classmethod
    def build_aston(cls,regno):
        g = cls("Marton",2342,regno)
        g.start()
        return g
    
    @staticmethod
    def get_anything():
        print("I am all Independent")