def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Iterate through the array starting from the second last element
    for i in range(len(arr) - 1):
        # Check if the current element is greater than or equal to the previous one
        if arr[i] >= arr[i + 1]:
            # Return the current index if found
            return i

    # If no such index is found, return -1
    return -1