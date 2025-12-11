def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)  # Join all elements in the list into a single string using Python's built-in join method

# Test cases
assert concatenate([]) == ''
assert concatenate(['a', 'b', 'c']) == 'abc'  # Ensure the function works as expected with different input lists
```