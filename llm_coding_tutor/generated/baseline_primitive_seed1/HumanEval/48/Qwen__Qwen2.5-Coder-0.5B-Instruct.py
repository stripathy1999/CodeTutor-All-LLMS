def is_palindrome(text: str) -> bool:
    return text == text[::-1]

# check function
def check():
    assert is_palindrome('') == True, "Test case 1 failed"
    assert is_palindrome('aba') == True, "Test case 2 failed"
    assert is_palindrome('aaaaa') == True, "Test case 3 failed"
    assert is_palindrome('zbcd') == False, "Test case 4 failed"
    print("All test cases passed!")

check()
```

This code snippet defines a function `is_palindrome` that checks if a given string is a palindrome. It uses slicing to reverse the string and compares it to the original. The `check` function tests various cases to ensure the correctness of the solution.