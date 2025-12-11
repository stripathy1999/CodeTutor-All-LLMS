def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Check if the input is None or an empty string
    if not string or string == '':
        return 0

    # Calculate the length of the string
    return len(string)