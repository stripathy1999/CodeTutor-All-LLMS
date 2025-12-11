def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # Iterate through the string, keeping track of the current stack.
    stack = []
    
    for char in string:
        if char == '[':
            # Push the opening bracket onto the stack.
            stack.append(char)
        elif char == ']':
            # If the stack is empty, it means there's no matching opening bracket.
            if not stack:
                return False
            # Pop the last opening bracket from the stack.
            stack.pop()
    
    # If the stack is empty, all brackets were matched and nested.
    return len(stack) == 0

# Test cases to verify the correctness of the function.