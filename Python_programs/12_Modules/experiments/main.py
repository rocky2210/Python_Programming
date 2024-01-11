import libr
# from libr.User import get_user
import libr.User as libuser
# import libr.Car as car
from libr.Car import Car
from libr.Bike import Bike
from libr.Automobile import Automobile


print(libr.add(5,6))
print(libuser.get_user("Mathi"))

x = Car("BMW","3434","TZ1323")
y = Car("WV","3434","TZ1323")

x.start()
y.start()

x.batt = 54

# Call with instance
x.get_battery()

# Call with class
Car.get_battery(x)

print(Car.type)

Car.get_type()  # Class method
Car.get_anything() # Static method

a = Car.build_aston("Tz34342")

print(a.carmake)
a.carmake = "Hello"

print(a.carmake)

a.start()
del a.carmake

print("A's type "+a.type)
Car.type = "benz"
q = Car.build_aston("Tn207657")
print(q.type)
q.type = "benz"
print(q.type)
print(Car.type) #class attribute


d = Bike("KTM","Duke","Tn23232")
d.carmake = "KTM TM"
print(d.carmake)

e = Automobile("KTM","Duke","Tn23232")
e.carmake = "KTM TM"
print(e.carmake)

c = Car.build_from_automobile(e)
c.start()