def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the list is empty
    if not l:
        return True

    # Determine the direction of the list
    is_decreasing = all(x > y for x, y in zip(l, l[1:]))
    is_increasing = all(x < y for x, y in zip(l, l[1:]))

    return is_decreasing or is_increasing
# NOTE: Rubric corruption applied, dropped 1 hints
