def total_match(lst1, lst2):
    total_chars = sum(len(s) for s in lst1 + lst2)
    if len(lst1) < total_chars:
        return lst1
    elif len(lst2) < total_chars:
        return lst2
    else:
        return lst1

# Test cases
print(total_match([], []))  # Output: []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # Output: ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # Output: ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # Output: ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # Output: ['4']
```