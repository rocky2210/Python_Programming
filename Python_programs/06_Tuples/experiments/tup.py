#Tuples are immutable lists
#The syntax uses () instead of []
t = (1,2,3,4,5,6,7,8,9)
print(t[2])
print(t[2:7])
print(t[7:2:-1])
print("---------------------------------")

t = (1,2,3,4,5,6,7,[1,2,3,4],8,9)
print(t)
t[7].append(5)
print(t)
print("---------------------------------")


a = (1,2,3,4)
h = (1,2,3,4)
print(id(a))
print(id(h))
print(a is h)
#Address :immutable , Data : immutable 
print("---------------------------------")


# Packing and unpacking
a = 0
b = 0
c = 0
t = (1,2,3)
a,b,c = t # type 1
print(a)
print(b)
print(c)

t = (1,2,3,4)
a,*b,c = t #type 2 (merge as list)
print(a)
print(b)
print(c)


a =10
b = 20
a,b = (b,a)
print(a)
print(b)
a =10
b = 20
a,b = b,a  #becoming a tuple and gets unpacked.
print(a)
print(b)
print("---------------------------------")


