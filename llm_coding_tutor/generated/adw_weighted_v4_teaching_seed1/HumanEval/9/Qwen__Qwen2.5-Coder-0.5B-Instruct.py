def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling max elements
    rolling_max_elements = []

    # Iterate through each number in the input list
    for num in numbers:
        # If the current number is greater than the last maximum element in the rolling max list,
        # append it to the rolling max list
        if num > rolling_max_elements[-1]:
            rolling_max_elements.append(num)

    return rolling_max_elements

# Example usage
print(rolling_max([1, 2,