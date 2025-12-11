def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Check if the list is empty
    if not l:
        raise ValueError("The list must contain at least one element.")
    
    # Sort the list
    l.sort()
    
    # Calculate the median
    mid = len(l) // 2
    if len(l) % 2 == 1:
        # Odd length list
        median = l[mid]
    else:
        # Even length list
        median = (l[mid - 1] + l[mid]) / 2
    
    return median

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0