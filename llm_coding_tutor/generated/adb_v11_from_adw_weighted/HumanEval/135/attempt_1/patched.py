def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is not greater than or equal to the previous element
        if arr[i] < arr[i - 1]:
            return i  # Return the index of the first element that violates the condition
    return -1  # Return -1 if no such element exists