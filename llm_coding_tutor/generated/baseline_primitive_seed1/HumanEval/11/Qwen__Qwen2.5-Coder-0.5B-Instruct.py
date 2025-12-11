def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_result = ""
    for char in a:
        if char == '0':
            xor_result += '1'
        elif char == '1':
            xor_result += '0'
        else:
            xor_result += char
    return xor_result

# Test cases
assert string_xor('010', '110') == '100'
assert string_xor('111', '000') == '111'
assert string_xor('000', '000') == '000'
assert string_xor('1111', '1111') == '0000'
assert string_xor('001', '001') == '000'  # This should be handled by the function correctly
```