# Open an existing file in append mode
with open("append.txt", "a") as file:
    # Append text to the file
    file.write("\nThis text will be appended to the file.\n")