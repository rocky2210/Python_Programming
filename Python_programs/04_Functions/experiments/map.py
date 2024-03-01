# First class instance
def create_adder(x):
    def adder(y):
        return x + y
    def sub(y):
        return x - y
    return adder,sub

add_40, sub_40 = create_adder(40) #A function with x = 40 is created and saved
print(add_40(100))
print(sub_40(200))
print(add_40(300))

l = [100,120,1000,1120]
print(list(map(add_40,l)))
print(list(map(sub_40,l)))

"""
    Output:
        140
        -160
        340
        [140, 160, 1040, 1160]
        [-60, -80, -960, -1080]
"""