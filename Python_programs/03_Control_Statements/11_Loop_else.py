count = 1
while count <= 5:
    print(count)
    if count == 3:
        break   # Exit the loop when count is 3
    count += 1
else:
    print("Loop completed without a 'break' statement.")
    
# ------------------------------------------
print("-------------------------------------")
for x in range(6):
    print(x)
else:
    print("Finally finished")