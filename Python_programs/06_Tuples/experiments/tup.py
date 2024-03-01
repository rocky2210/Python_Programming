#Tuples are immutable lists
#The syntax uses () instead of []
t = (1,2,3,4,5,6,7,8,9)
print(t[2])
# Output: 3
print(t[2:7])
# Output: (3, 4, 5, 6, 7)
print(t[7:2:-1])
# Output: (8, 7, 6, 5, 4)
print("---------------------------------")

t = (1,2,3,4,5,6,7,[1,2,3,4],8,9)
print(t)
t[7].append(5)
print(t)
# Output: (1, 2, 3, 4, 5, 6, 7, [1, 2, 3, 4, 5], 8, 9)
print("---------------------------------")


a = (1,2,3,4)
h = (1,2,3,4)
print(id(a))
# Output: 140442462340304
print(id(h))
# Output: 140442462357168
print(a is h)
# Output: False
#Address :immutable , Data : immutable 
print("---------------------------------")


# Packing and unpacking
a = 0
b = 0
c = 0
t = (1,2,3)
a,b,c = t # type 1
print(a)
# Output: 1
print(b)
# Output: 2
print(c)
# Output: 3

t = (1,2,3,4)
a,*b,c = t #type 2 (merge as list)
print(a)
# Output: 1
print(b)
# Output: [2, 3]
print(c)
# Output: 4


a =10
b = 20
a,b = (b,a)
print(a)
# Output: 20
print(b)
# Output: 10
a =10
b = 20
a,b = b,a  #becoming a tuple and gets unpacked.
print(a)
# Output: 20
print(b)
# Output: 10
print("---------------------------------")


