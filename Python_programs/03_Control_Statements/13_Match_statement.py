# A match statement

"""
    Match statement:
        The match statement in Python is a feature introduced in Python 3.10 as 
        part of PEP 634 (Pattern Matching). It provides a powerful and concise syntax 
        for performing pattern-based conditional execution, making code more readable and expressive.
        
        Usage:
            The match statement is particularly useful when dealing with complex conditional logic 
            involving multiple possible patterns or conditions. It simplifies code and makes it more 
            readable by clearly expressing the different cases or scenarios being handled.
"""


def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number"
print(weekday(3))
print(weekday(6))
print(weekday(7))

"""
    Output:
        Thursday
        Sunday
        Invalid day number
"""
print("--------------------------------")



# Combined cases
def access(user):
    match user:
        case "admin" | "manager" : return "Full access"
        case "guest" : return "Limited access"
        case _: return "No access"
print(access("manager"))
print(access("guest"))
print(access("rocky"))

"""
    Output:
        Full access
        Limited access
        No access
"""
print("--------------------------------")


# List as the argument
def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time , *names]:
            msg = ''
            for name in names:
                msg+= f'Good {time} {name}!\n'
            return msg
print(greeting(["Morning", "Rocky"]))
print(greeting(["Afternoon", "Virat"]))
print(greeting(["Evening", "Kanna", "Baby", "Gayu"]))

"""
    Output:
        Good Morning Rocky!
        Good Afternoon Virat!
        Good Evening Kanna!
        Good Evening Baby!
        Good Evening Gayu!
"""

