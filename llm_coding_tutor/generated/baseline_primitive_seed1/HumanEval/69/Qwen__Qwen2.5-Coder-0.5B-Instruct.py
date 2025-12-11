from collections import Counter

def search(lst):
    count = Counter(lst)
    for num in lst:
        if count[num] >= num:
            return num
    return -1

# Test cases
assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1
```

This solution introduces a different approach by using `Counter` from the `collections` module to efficiently count the occurrences of each integer in the list. It then iterates through the list again, checking if each integer's frequency is greater than or equal to its value, returning the first such integer it encounters. If no such integer is found, it returns -1.