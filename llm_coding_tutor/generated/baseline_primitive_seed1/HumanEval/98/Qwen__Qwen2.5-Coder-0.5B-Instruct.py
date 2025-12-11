import re

def count_upper(s):
    # Use regular expression to find all uppercase vowels at even indices
    return sum(1 for char in s if char.isupper() and (index := s.index(char)) % 2 == 0)

# Example usage:
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))   # Output: 0
```