from typing import *
from collections import *

def string_sequence(n: int) -> str:
    return''.join(map(str, range(n + 1)))

# Test cases
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```