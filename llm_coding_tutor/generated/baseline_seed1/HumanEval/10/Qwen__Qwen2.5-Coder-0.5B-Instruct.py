```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Helper function to check if a string is a palindrome
    def is_palindrome_helper(s):
        return s == s[::-1]

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome_helper(string[i:]):
            # Reverse the prefix that comes before the palindrome
            prefix = string[:i]
            # Append to the end of the string
            return string + prefix[::-1]

    # If no palindrome is found, return an empty string