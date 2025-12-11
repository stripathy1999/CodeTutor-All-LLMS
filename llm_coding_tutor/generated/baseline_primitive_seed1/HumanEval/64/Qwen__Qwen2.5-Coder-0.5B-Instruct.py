from typing import *
from collections import *

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = set('aeiouAEIOU')
    count = sum(1 for char in s if char in vowels)
    if s.endswith('y'):
        count += 1
    return count

# Test cases
assert vowels_count("abcde") == 2
assert vowels_count("ACEDY") == 3
assert vowels_count("yak") == 0
assert vowels_count("quickly") == 1
assert vowels_count("sky") == 1
assert vowels_count("FULL") == 3
assert vowels_count("quickly") == 1
assert vowels_count("Sky") == 1
assert vowels_count("