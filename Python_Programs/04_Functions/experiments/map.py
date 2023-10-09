def create_adder(x):
    def adder(y):
        return x + y
    def sub(y):
        return x - y
    return adder,sub

add_40 , sub_40 = create_adder(40) 
# print(add_40(100))
# print(add_40(200))
# print(add_40(300))
# print(sub_40(2))
# print(sub_40(3))
# print(sub_40(2))

l = [100,120,1000,1120]
# for i in l:
#     print(add_40(i))
#     print(sub_40(i))

print(list(map(add_40,l)))
print(list(map(sub_40,l)))

