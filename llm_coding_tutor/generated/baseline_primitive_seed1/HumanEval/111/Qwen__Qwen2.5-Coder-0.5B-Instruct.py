from collections import Counter

def histogram(test):
    counts = Counter(test.split())
    max_count = max(counts.values())
    result = {letter: count for letter, count in counts.items() if count == max_count}
    return result

# Test cases
print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}