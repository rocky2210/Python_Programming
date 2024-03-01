def double_numbers(iterable):
    for i in iterable:
        print(f"[] double data gen {i}")
        yield i * 2
        
i = double_numbers(range(1,30))

k = next(i)
while k:
    print(k)
    try:
        k = next(i)
    except:
        break
    
"""
    Output:
        [] double data gen 1
        2
        [] double data gen 2
        4
        [] double data gen 3
        6
        [] double data gen 4
        8
        [] double data gen 5
        10
        [] double data gen 6
        12
        [] double data gen 7
        14
        [] double data gen 8
        16
        [] double data gen 9
        18
        [] double data gen 10
        20
        [] double data gen 11
        22
        [] double data gen 12
        24
        [] double data gen 13
        26
        [] double data gen 14
        28
        [] double data gen 15
        30
        [] double data gen 16
        32
        [] double data gen 17
        34
        [] double data gen 18
        36
        [] double data gen 19
        38
        [] double data gen 20
        40
        [] double data gen 21
        42
        [] double data gen 22
        44
        [] double data gen 23
        46
        [] double data gen 24
        48
        [] double data gen 25
        50
        [] double data gen 26
        52
        [] double data gen 27
        54
        [] double data gen 28
        56
        [] double data gen 29
        58
"""