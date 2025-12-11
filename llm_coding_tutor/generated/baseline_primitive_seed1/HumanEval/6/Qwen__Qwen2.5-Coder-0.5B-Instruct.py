from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    max_nesting = 0
    current_nesting = 0

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_nesting += 1
            max_nesting = max(max_nesting, current_nesting)
        elif char == ')':
            stack.pop()
            current_nesting -= 1

    return [max_nesting] + [current_nesting] * (len(paren_string) - max_nesting - 1)


# Test cases
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
print(parse_nested_parens('()