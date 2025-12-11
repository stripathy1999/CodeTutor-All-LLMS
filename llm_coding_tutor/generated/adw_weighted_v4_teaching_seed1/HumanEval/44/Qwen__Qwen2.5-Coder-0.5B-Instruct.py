def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base."""
    if not (0 <= base <= 9):
        raise ValueError("Base must be between 1 and 9.")
    
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base
    
    return result

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'