def concatenate\(strings: List\[str\]\) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate\(\[\]\)
    ''
    >>> concatenate\(\['a', 'b', 'c'\]\)
    'abc'
    """
    if not strings:
        return ''
    elif len\(strings\) == 1:
        return strings\[0\]
    else:
        return ''\.join\(strings\)