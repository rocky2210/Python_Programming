def double_numbers(iterable):
    for i in iterable:
        print(f"[] double data gen {i}")
        yield i * 2  #Lazycoding
        
# def double_numbers(iterable):
#     l = []
#     for i in iterable:
#         print("[] double data gen ()".format(i))
#         l.append(i*2)
#     return l

def datagen():
    l = []
    for i in range(100):
        print("[] data gen")
        l.append(i)
    return l

# Generating the data on-demand
for i in double_numbers(range(100)):
    print(i)
    
# Iterating already available data
for i in datagen():
    print(i)