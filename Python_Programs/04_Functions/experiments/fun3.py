def add(x,*y): #Variable number of positional arguments
    
    print(x)
    print(y)
    
    r = 0
    r = r + x
    for i in y:
        r = r + i
    return r

# both functions works as same ...!

def addone(*y): 
    x = 0
    print(x)
    print(y)
    r = 0
    r = r + x
    for i in y:
        r = r + i
    return r

print("Addition result : {}".format(addone(1,2,3,4,5,6,7)))

