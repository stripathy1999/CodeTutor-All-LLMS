from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove all elements that occur more than once from a list of integers.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result