# Open the file in read mode
with open ("read.txt", "r") as file:
    # Read and print each line
    for line in file:
        print(line.strip()) # Use strip() to remove newline characters
        