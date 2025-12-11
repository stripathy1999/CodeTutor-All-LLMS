def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list to make it easier to find the closest elements
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to store the closest pair
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        current_distance = sorted_numbers[i + 1] - sorted_numbers[i]
        if current_distance < closest_pair[1] - closest_pair[0]:
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair