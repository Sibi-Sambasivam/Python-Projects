def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

input_type = input("Enter 'b' for binary to decimal or 'd' for decimal to binary: ")
if input_type == 'b':
    binary_input = input("Enter a binary number: ")
    print("Decimal:", binary_to_decimal(binary_input))
elif input_type == 'd':
    decimal_input = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(decimal_input))
else:
    print("Invalid input.")
