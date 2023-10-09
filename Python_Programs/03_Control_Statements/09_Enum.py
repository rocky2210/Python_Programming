l = ['apple','orange','banana','kiwi']
print(type(l))
print(type(enumerate(l)))

e= enumerate(l)
for i,v in e:
    print("#{} {}".format(i,v))

#__next__
l = ['apple','pineapple','gauva','cherry']
k= enumerate(l)
for h in range(len(l)):
    print(k.__next__())
