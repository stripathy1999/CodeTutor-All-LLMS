def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]  # Initialize the result with the first number in the list
    for number in numbers[1:]:
        if number > result[-1]:  # If the current number is greater than the last number in the result
            result.append(number)  # Append the current number to the result
        else:
            result[-1] = max(result[-1], number)  # Update the last element in the result
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```