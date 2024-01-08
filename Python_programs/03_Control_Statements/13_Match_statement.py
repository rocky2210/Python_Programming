# A match statement takes an expression and compares its 
# value to successive patterns given as one or more case blocks.
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
print(greeting(["Afternoon", "Dora"]))
print(greeting(["Evening", "Inu", "Baby", "thire"]))

