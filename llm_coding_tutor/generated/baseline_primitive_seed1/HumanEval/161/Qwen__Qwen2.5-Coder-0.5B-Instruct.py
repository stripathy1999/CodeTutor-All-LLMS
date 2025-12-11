def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    return ''.join(char.swapcase() if char.isalpha() else char for char in s) 

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))   # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c" 
```