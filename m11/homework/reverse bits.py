# Program to reverse all bits of a number

# Take user input
num = int(input("Enter a number: "))

# Convert number to binary (remove '0b')
binary_str = bin(num)[2:]

# Reverse the binary string
reversed_binary = binary_str[::-1]

# Convert reversed binary back to integer
reversed_number = int(reversed_binary, 2)

# Output the result
print("Reversed Bits Number:", reversed_number)
