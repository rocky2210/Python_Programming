# Writing binary data to a file
with open("binary.bin", "wb") as binary_file:
    binary_file.write(b'\x48\x65\x6C\x6C\x6F')  # Binary data for "Hello"

# Reading binary data from a file
with open("binary.bin", "rb") as binary_file:
    data = binary_file.read()
    print(data)  # Output: b'Hello'
