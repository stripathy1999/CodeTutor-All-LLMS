from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Calculate the difference between consecutive elements
    differences = [sorted_numbers[i+1] - sorted_numbers[i] for i in range(len(sorted_numbers)-1)]
    
    # Find the minimum difference
    min_diff = min(differences)
    
    # Find the indices of the minimum difference
    min_index = differences.index(min_diff)
    
    # Return the two closest elements
    return sorted