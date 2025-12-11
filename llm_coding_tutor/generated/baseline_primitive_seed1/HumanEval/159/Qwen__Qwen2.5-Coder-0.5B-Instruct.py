def eat(number, need, remaining):
    total_eaten = number
    total_remaining = remaining
    if number >= need:
        total_eaten += need
        total_remaining -= need
    else:
        total_eaten += remaining
        total_remaining = 0
    return [total_eaten, total_remaining]

# Example usage:
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))  # Output: [12, 1]
print(eat(1, 10, 10))  # Output: [11, 0]
print(eat(2, 11, 5))  # Output: [7, 0]
```