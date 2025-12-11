from typing import List

def median(l: List) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list
    sorted_list = sorted(l)
    # Get the number of elements in the list
    num_elements = len(sorted_list)
    # Check if the number of elements is odd or even
    if num_elements % 2 == 1:
        # Return the middle element
        return sorted_list[num_elements // 2]
    else:
        # Return the average of the two middle elements
        mid1 = sorted_list[num_elements // 2 - 1]
        mid2 = sorted_list[num_elements // 2]
        return (mid1 + mid2) / 2.0

# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1