def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift
    effective_shift = shift % len(x_str)
    
    # Perform the circular shift
    if effective_shift == 0:
        # If shift is zero, return the original string
        return x_str
    else:
        # Perform the circular shift
        shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
        return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"