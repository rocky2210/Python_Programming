# Loop else

"""
    Loop else:
        the else clause can be used in conjunction with loops, including for loops and while loops. 
        The else block associated with a loop is executed when the loop completes all its iterations 
        without encountering a break statement.
"""

count = 1
while count <= 5:
    print(count)
    if count == 3:
        break   # Exit the loop when count is 3
    count += 1
else:
    print("Loop completed without a 'break' statement.")
    
"""
    Output:
        1
        2
        3
"""
# ------------------------------------------
print("-------------------------------------")
for x in range(6):
    print(x)
else:
    print("Finally finished")
    
""" 
    Output:
        0
        1
        2
        3
        4
        5
        Finally finished
"""