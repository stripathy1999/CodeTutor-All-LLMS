from typing import *
from collections import *

def remove_vowels(text: str) -> str:
    return ''.join([char for char in text if char not in 'aeiouAEIOU'])

# Test cases
assert remove_vowels('') == ''
assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
assert remove_vowels('abcdef') == 'bcdf'
assert remove_vowels('aaaaa') == ''
assert remove_vowels('aaBAA') == 'B'
assert remove_vowels('zbcd') == 'zbcd' 

print(remove_vowels('abcde'))  # Expected output: 'bcd'
print(remove_vowels('bcdf'))   # Expected output: 'bcd'
print(remove_vowels('abcdefg')) # Expected output: 'bcdfg'
print(remove_vowels('Hello World!')) # Expected output: 'Hll Wrld!'
print(remove_vowels('1234567890')) # Expected output: '1234567890'
```