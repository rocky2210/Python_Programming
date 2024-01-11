file_name = input("Enter a file name or path to read :")
f = open(file_name,'r')
print(f.read())
f.close()

"""
    Output
        python file.py
        Enter a file name or path to read :dummy.txt
"""