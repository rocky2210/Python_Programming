try:
    with open("nonexistent_file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occured: {e}")

"""
    Output:
        The file does not exist.
"""