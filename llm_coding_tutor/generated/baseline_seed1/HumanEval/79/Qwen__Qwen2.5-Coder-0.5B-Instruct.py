```python
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    # Convert the decimal number to binary using Python's built-in function
    binary_representation = bin(decimal)[2:]  # [2:] removes the '0b' prefix
    
    # Format the binary representation with 'db' at the beginning and end
    formatted_binary = f"db{binary_representation}db"
    
    return formatted_binary

# Test cases
print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db1000