def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return i
    return -1

# Test cases
print(can_arrange([1,2,4,3,5]))  # Expected output: 3
print(can_arrange([1,2,3]))       # Expected output: -1
print(can_arrange([5,4,3,2,1]))  # Expected output: 2
print(can_arrange([1,2,3,4,5]))  # Expected output: 0
print(can_arrange([1,1,1,1,1]))  # Expected output: -1
```