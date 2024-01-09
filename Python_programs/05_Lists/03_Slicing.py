#var[start:stop-1:step] => list/collection
""" 
step = 1
start = 0
stop = len()
"""

l = [1,2,3,4,5,6,7,8,9]
a = l[1:5:1]
print(a)
print("------------------------------------")

a = l [::-1]
print(a)
print("------------------------------------")

a = l [0:len(l):1]
print(a)
print("------------------------------------")

m = l 
print(id(l))
print(id(m))
print("------------------------------------")

m = l.copy()
print(id(l))
print(id(m))
print("------------------------------------")

# Deep layer copy
m = l[::1]
print(id(l))
print(l)
print(m)
print(id(m))
print("------------------------------------")


l = [1,2,[1,2,3],4,5,6]
print(l)
u = l[::1]
print(id(l))
print(id(u)) #different address
l[2].append(4)
print(l)
print(u)
for i in range(len(l)):
    print("#{} : l->{}, ID->{}".format(i,l[i],id(l[i])))
    print("#{} : u->{}, ID->{}".format(i,u[i],id(u[i])))
    #same address
print("------------------------------------")

import copy
l = [1,2,[1,2,3],4,5,6]
l[2].append([5,6,7])
u = l[::1]
print(l)
print(u)
u = copy.deepcopy(l)
for i in range(len(l)):
    print("#{} : l->{}, ID->{}".format(i,l[i],id(l[i])))
    print("#{} : u->{}, ID->{}".format(i,u[i],id(u[i])))
    #same address
print("------------------------------------")

l[2][3].append(8)
print(l)
print(u)
#deep copy

# More slicing
#Slicing
l = list(range(0,100))
print(l)
print(l[0:30])
print(l[::-1])
print(l[30:0:-2])
print(l[30:50:2])