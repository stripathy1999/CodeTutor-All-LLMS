from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    # Remove strings with odd lengths
    even_length_words = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the words by length and then alphabetically
    sorted_words = sorted(even_length_words, key=lambda x: (len(x), x))
    
    return sorted_words

# Test cases
assert list_sort(["aa", "a", "aaa"]) == ["aa"]
assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```