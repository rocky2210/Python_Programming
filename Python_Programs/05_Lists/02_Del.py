#del keyword
"""
It deletes an items inside a list or it can delete an entire variable 
"""
u = [1, 2, [1, 2, 3, [5, 6, 7]], 4, 5, 6,7]
u.remove(1)
print(u)
del u[3]
print(u)

#in keyword
print(2 in u) #true
print("hello" in u) #false

