from typing import *
from collections import *

def maximum(arr: List[int], k: int) -> List[int]:
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Take the first k elements from the sorted array
    result = arr[:k]
    
    return result