from typing import *
from collections import *

def modp(n: int, p: int) -> int:
    return pow(2, n, p)

# test cases
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```