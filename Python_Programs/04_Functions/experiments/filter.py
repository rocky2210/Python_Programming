l = [100,120,1000,1120]

print(list(filter((lambda x : x >= 1000 ),l)))


l = [100,120,1000,1120]
def fil(x):
    return x >= 1000

print(list(filter(fil, l)))
