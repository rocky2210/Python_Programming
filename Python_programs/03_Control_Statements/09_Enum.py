l = ['apple','orange','banana','kiwi']
print(type(l))
print(type(enumerate(l)))

e = enumerate(l)
for i,v in e:
    print(f"#{i} {v}")
    
# __next__
l = ['apple','orange','banana','kiwi']
k = enumerate(l)
for h in range(len(l)):
    print(k.__next__())