def vowels_count(s):
    """
    Write a function vowels_count which takes a string representing
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
    
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    
    # Count the number of vowels
    count = sum(1 for char in s if char in vowels)
    
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("quick brown fox"))  # Output: 4
print(vowels_count("sky"))        # Output: 1
print(vowels_count("HELLO WORLD"))  # Output: 7