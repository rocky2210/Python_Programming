# Define two integers for bitwise operations
a = 0b1100  # Binary representation of 12
b = 0b1010  # Binary representation of 10

# Bitwise AND
result_and = a & b  # 0b1000 (Binary) => 8 (Decimal)
print("Bitwise AND:", bin(result_and),":", result_and)

# Bitwise OR
result_or = a | b  # 0b1110 (Binary) => 14 (Decimal)
print("Bitwise OR:", bin(result_or),":", result_or)

# Bitwise XOR
result_xor = a ^ b  # 0b0110 (Binary) => 6 (Decimal)
print("Bitwise XOR:", bin(result_xor),":", result_xor)

# Bitwise NOT (applied to 'a')
result_not_a = ~a  # -13 (Decimal)
print("Bitwise NOT (a):", bin(result_not_a),":", result_not_a)

# Left Shift 'a' by 2 positions
result_left_shift = a << 2  # 0b110000 (Binary) => 48 (Decimal)
print("Left Shift:", bin(result_left_shift),":", result_left_shift)

# Right Shift 'a' by 2 positions
result_right_shift = a >> 2  # 0b11 (Binary) => 3 (Decimal)
print("Right Shift:", bin(result_right_shift),":", result_right_shift)


"""
Bin() - returns binary representations of the integer.
"""

"""
    Output:
        Bitwise AND: 0b1000 : 8
        Bitwise OR: 0b1110 : 14
        Bitwise XOR: 0b110 : 6
        Bitwise NOT (a): -0b1101 : -13
        Left Shift: 0b110000 : 48
        Right Shift: 0b11 : 3
"""