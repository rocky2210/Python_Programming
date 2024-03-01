# Break statement

"""
    Break statement:
        The break statement is used in Python to terminate the execution of a loop prematurely, 
        regardless of whether the loop's condition is still true or not. It's commonly used to 
        exit a loop when a certain condition is met before the loop reaches its natural end.
"""
count = 1
while count <= 5:
    print(count)
    if count == 3:
        break   # Exit the loop when count is 3
    count += 1
    
"""
    Output:
        1
        2
        3
"""