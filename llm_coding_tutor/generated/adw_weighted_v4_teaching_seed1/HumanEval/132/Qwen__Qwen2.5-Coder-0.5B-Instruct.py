def is_nested(string):
    depth = 0
    nested = False

    for char in string:
        if char == '[':
            depth += 1
            if depth > 1:  # At least one bracket must be nested
                nested = True
        elif char == ']':
            depth -= 1

    return nested and depth == 0

# Test cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))   # False
print(is_nested('[]'))     # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True