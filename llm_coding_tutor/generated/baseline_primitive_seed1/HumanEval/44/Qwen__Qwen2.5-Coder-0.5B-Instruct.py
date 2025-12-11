def change_base(x: int, base: int) -> str:
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    
    if x == 0:
        return "0"
    
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    
    # Reverse the list to get the correct order
    digits.reverse()
    
    return ''.join(digits)

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python function `change_base` takes two parameters, `x` and `base`, and returns a string representing the number `x` in the specified base. It includes error handling for base values that are not within the allowed range (2 to 9). The function works by repeatedly dividing `x` by `base` and collecting the remainders, which are the digits of the number in the new base. Finally, it reverses the list to get the digits in