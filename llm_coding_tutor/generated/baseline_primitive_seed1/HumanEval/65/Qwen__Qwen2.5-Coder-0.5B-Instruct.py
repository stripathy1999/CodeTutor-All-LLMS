def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == len(str(x)):
        return str(x)[::-1]
    
    # Calculate effective shift using modulo to handle cases where shift is greater than the length of x
    effective_shift = shift % len(str(x))
    
    # Perform the circular shift
    shifted_digits = str(x)[-effective_shift:] + str(x)[:effective_shift]
    
    return shifted_digits

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```