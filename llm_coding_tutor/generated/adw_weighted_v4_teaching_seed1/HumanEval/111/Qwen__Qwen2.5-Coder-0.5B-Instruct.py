def histogram(test):
    from collections import Counter
    from typing import List
    
    # Count the occurrences of each character in the string
    char_counts = Counter(test)
    
    # Find the maximum occurrence count
    max_count = max(char_counts.values())
    
    # Collect characters that have the maximum occurrence count
    result = {char: count for char, count in char_counts.items() if count == max_count}
    
    return result

# Test cases
print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}