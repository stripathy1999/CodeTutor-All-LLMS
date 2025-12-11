from typing import *
from collections import *

def get_closest_vowel(word: str) -> str:
    vowels = set("aeiouAEIOU")
    closest_vowel = ""
    for i in range(len(word) - 2):
        if word[i] not in vowels and word[i + 1] not in vowels and word[i + 2] not in vowels:
            closest_vowel = word[i]
            break
    return closest_vowel

# check function with provided data points
assert get_closest_vowel("yogurt") == "u", "Test case 1 failed"
assert get_closest_vowel("FULL") == "U", "Test case 2 failed"
assert get_closest_vowel("quick") == "", "Test case 3 failed"
assert get_closest_vowel("ab") == "", "Test case 4 failed"
```