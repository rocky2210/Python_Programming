#Tuples are immutable lists
#The syntax uses () instead of []
t = (1,2,3,4,5,6,7,8,9)
print(t[2])
print(t[2:7])
print(t[7:2:-1])

t = (1,2,3,4,5,6,7,[1,2,3,4],8,9)
print(t)
t[7].append(5)
print(t)