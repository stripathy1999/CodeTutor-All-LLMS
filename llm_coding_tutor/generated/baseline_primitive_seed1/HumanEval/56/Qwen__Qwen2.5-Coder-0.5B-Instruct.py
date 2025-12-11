import re

def correct_bracketing(brackets: str) -> bool:
    # Use regular expression to find all occurrences of "<" and ">"
    pattern = re.compile(r'<[^>]*>|>[^<]*>')
    matches = pattern.findall(brackets)
    
    # Check if the number of matches is exactly 1
    return len(matches) == 1

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```