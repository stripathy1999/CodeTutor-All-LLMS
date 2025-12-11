from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Handle edge cases
    if not strings:
        return ''
    
    # Use join method to concatenate strings
    result = ''.join(strings)
    return result