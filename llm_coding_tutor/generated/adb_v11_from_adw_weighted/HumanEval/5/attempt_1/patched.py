from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the input list
    for i in range(len(numbers)):
        # Append the current element to the result list
        result.append(numbers[i])
        
        # Check if it's the last element or the next element should be separated by the delimiter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    return result