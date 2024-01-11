file_name = input("Enter a file name or path to read:")
f = open(file_name,'r')
i = 0
line = f.readline()
while line:
    line = f.readline()
    print(line,end="")
    if i % 10 == 0:
        op = input("read more ? [n]:")
        if op == 'n':
            print("Existing...")
            break
    i = i+1
f.close()

