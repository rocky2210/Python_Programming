#anonymous functions aka lambda functions

# ordinary function:
def check (x):
    return x > 3

# lambda function:
y = (lambda x : x > 3)(5)

# check(5)
print(y)