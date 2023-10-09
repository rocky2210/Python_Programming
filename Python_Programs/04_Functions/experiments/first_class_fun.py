#first class instance

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_40 = create_adder(10) #A function with x = 10 is created and saved
print(add_40(100))
print(add_40(200))
print(add_40(300))

print("----------------")

def create_adder(x):
    def adder(y):
        return x + y
    def sub(y):
        return x - y
    return adder,sub

add_40 , sub_40 = create_adder(10) 
print(add_40(100))
print(add_40(200))
print(add_40(300))
print(sub_40(2))
print(sub_40(3))
print(sub_40(2))


