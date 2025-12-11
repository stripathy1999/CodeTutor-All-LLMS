from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]

    for str in strings:
        if len(str) > len(longest_str):
            longest_str = str

    return longest_str

# check function to verify the correctness
def check_longest():
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['aa', 'bb', 'cc']) == 'bb'
    assert longest(['a', 'bb', 'ccc', 'ddd']) == 'ddd'

check_longest()
```