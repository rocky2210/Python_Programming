# Continue Statement

"""
    Continue Statement:
        The continue statement is used within loops to skip the rest 
        of the code inside the loop for the current iteration and move 
        to the next iteration. Unlike the break statement, which completely 
        exits the loop, continue only interrupts the current iteration and 
        continues with the next iteration of the loop.
"""

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
"""
    Output:
        1
        2
        4
        5
        6
"""