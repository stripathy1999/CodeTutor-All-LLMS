from typing import *
from collections import *

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Edge cases
    if not numbers or len(numbers) < 2:
        return False

    # Sort the numbers
    sorted_numbers = sorted(numbers)

    # Iterate through the sorted numbers
    for i in range(len(sorted_numbers) - 1):
        # Calculate the absolute difference between adjacent numbers
        diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])

        # Check if the difference is less than the threshold
        if diff < threshold:
            return True

    # If no close elements were found, return False
    return False