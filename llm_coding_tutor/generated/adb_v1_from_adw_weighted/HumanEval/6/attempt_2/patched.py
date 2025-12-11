def parse_nested_parens\(paren_string: str\) -> List\[int\]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces\.
    For each of the group, output the deepest level of nesting of parentheses\.
    E\.g\. \(\(\)\(\)\) has maximum two levels of nesting while \(\(\(\)\)\) has three\.

    >>> parse_nested_parens\('\(\(\)\(\)\) \(\(\(\)\)\) \(\) \(\(\(\)\)\(\)\(\)\)'\)
    \[2, 3, 1, 3\]
    """
    max_depth = 0
    current_depth = 0
    
    for char in paren_string:
        if char == '\(':
            # Increase current depth for an opening parenthesis
            current_depth \+= 1
            # Update max depth if current depth is greater
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == '\)':
            # Decrease current depth for a closing parenthesis
            current_depth -= 1
    
    # Return the list of maximum depths for each group
    return \[max_depth for _ in range\(len\(paren_string\)\)\]