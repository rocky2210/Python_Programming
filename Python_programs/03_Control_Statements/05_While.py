# While loop

"""
    While Loop:
        A while loop is a control flow statement that allows code to be executed repeatedly 
        based on a given condition. It continues to execute a block of code as long as the 
        condition remains true. The loop iterates over and over again until the condition evaluates to false
"""

count = 1
while count <=5:
    print(count)
    count +=1   # Increment the count by 1 in each iteration
"""
    Output:
        1
        2
        3
        4
        5
"""
"""
    1. initialize - var = 10
    2. condition - var <=10
    3. update code - var = var - 1
"""

"""
    var = 10
    while var >= 10: # Infinity loop
        print("Hello world")
"""

var = 10
while var <=10 and var >=0:
    print(f"#{var} Hello world")
    var = var -1
print("Loop exited")

# use while in arithmetic based condition

"""
    Output:
        #10 Hello world
        #9 Hello world
        #8 Hello world
        #7 Hello world
        #6 Hello world
        #5 Hello world
        #4 Hello world
        #3 Hello world
        #2 Hello world
        #1 Hello world
        #0 Hello world
        Loop exited
"""