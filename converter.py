def binary_to_decimal(binary):
    decimal = int(binary,2)
    return decimal

def binary_to_hex(binary):
    # Convert the binary number to an integer
    decimal = int(binary, 2)
    # Use the hex function to convert the decimal number to a hexadecimal number
    hexadecimal = hex(decimal)
    # Remove the "0x" prefix from the hexadecimal number
    hexadecimal = hexadecimal[2:]
    # Return the hexadecimal number as a string
    return hexadecimal.upper()

def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b","")
    return binary

def decimal_to_hex(decimal):
    # Use the hex function to convert the decimal number to a hexadecimal number
    hexadecimal = hex(decimal)
    # Remove the "0x" prefix from the hexadecimal number
    hexadecimal = hexadecimal[2:]
    # Return the hexadecimal number as a string
    return hexadecimal.upper()

def hex_to_binary(hexadecimal):
    # Convert the hexadecimal number to an integer
    decimal = int(hexadecimal, 16)
    # Use the bin function to convert the decimal number to a binary number
    binary = bin(decimal)
    # Remove the "0b" prefix from the binary number
    binary = binary[2:]
    # Return the binary number as a string
    return binary

def hex_to_decimal(hexadecimal):
    # Convert the hexadecimal number to a decimal integer
    decimal = int(hexadecimal, 16)
    # Return the decimal integer
    return decimal

