def double_numbers(iterable):
    for i in iterable:
        print(f"[] double data gen {i}")
        yield i * 2
        
i = double_numbers(range(1,100))

k = next(i)
while k:
    print(k)
    try:
        k = next(i)
    except:
        break