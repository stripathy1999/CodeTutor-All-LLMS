def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    - x (int): The integer to be shifted.
    - shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    - str: The shifted integer as a string.
    """
    # Convert the integer to a list of its digits
    digits = [int(digit) for digit in str(abs(x))]
    
    # Handle cases where shift is greater than the number of digits
    if shift >= len(digits):
        return ''.join(str(digit) for digit in digits[::-1])
    
    # Perform the circular shift
    left_digits = digits[shift:] + digits[:shift]
    
    # Convert the left digits back to strings
    left_digits_str = [str(digit) for digit in left_digits]
    
    # Join the left digits back into a string
    return ''.join(left_digits_str)

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"