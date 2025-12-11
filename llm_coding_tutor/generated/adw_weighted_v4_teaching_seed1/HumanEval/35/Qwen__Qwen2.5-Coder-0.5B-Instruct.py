import math

def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): List of elements to find the maximum of.
    
    Returns:
    int: The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    TypeError: If the list contains non-numeric elements.
    """
    if not l:
        raise ValueError("The list is empty.")
    
    if not all(isinstance(x, (int, float)) for x in l):
        raise TypeError("The list contains non-numeric elements.")
    
    max_value = l[0]
    for value in l:
        if value > max_value:
            max_value = value
    
    return max_value