def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()


# check function
assert flip_case('Hello') == 'hELLO', "Test case 1 failed"
assert flip_case('WorLD') == 'wORld', "Test case 2 failed"
assert flip_case('123abcABC') == '123ABCabc', "Test case 3 failed"
assert flip_case('aBcDeF') == 'AbCdEf', "Test case 4 failed"

print("All test cases passed!")