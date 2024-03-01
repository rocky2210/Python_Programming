# Recursion

"""
    Recursion:
        Recursion is a programming technique where a function calls itself in order to solve a problem. 
        It's a powerful and elegant approach that can be used to break down complex problems into simpler 
        subproblems. Recursion consists of two parts: the base case and the recursive case.
"""

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion example results")
tri_recursion(10)

"""
    Output:
        Recursion example results
        1
        3
        6
        10
        15
        21
        28
        36
        45
        55
"""