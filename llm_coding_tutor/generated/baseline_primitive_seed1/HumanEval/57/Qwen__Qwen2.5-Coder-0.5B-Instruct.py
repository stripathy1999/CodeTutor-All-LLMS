def monotonic(l: list):
    # Check if the list is empty or has only one element
    if len(l) <= 1:
        return True
    
    # Iterate through the list to check if it's monotonically increasing or decreasing
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
        elif l[i] > l[i - 1]:
            return True
    
    return True

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```