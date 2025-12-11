```python
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
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    # If the last character is 'y' and it's not at the end of the word, increment the count
    if s.endswith('y') and s[-1]!= 'y':
        count += 1
    
    return count

# Test cases
print(vowels_count("abcde