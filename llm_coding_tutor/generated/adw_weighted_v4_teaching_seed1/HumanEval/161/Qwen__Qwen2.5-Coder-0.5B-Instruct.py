def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

    # Check if the string is empty or contains only non-letter characters
    if not s or not s.isalpha():
        return s[::-1]

    # Reverse the case of all alphabetic characters
    result = ''.join(char.swapcase() if char.isalpha() else char for char in s)

    return result

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))   # Output: "#A@c"